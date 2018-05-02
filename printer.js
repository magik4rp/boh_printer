const { apiKey, messagingSenderId } = require('./constants')
const { debounce } = require('lodash')
var moment = require('moment')
var SerialPort = require('serialport'),
  serialPort = new SerialPort('/dev/serial0', {
    baudRate: 19200
  }),
  Printer = require('thermalprinter')
//hello
var path = __dirname + '/images/boh_small.png'
var printer, numMessages
var initialDataLoaded = true
var Gpio = require('onoff').Gpio //include onoff to interact with the GPIO
var LED1 = new Gpio(21, 'out', { debounceTimeout: 10 }) //display red
var LED2 = new Gpio(26, 'out', { debounceTimeout: 10 }) //display red
var LED3 = new Gpio(20, 'out', { debounceTimeout: 10 }) //blinking red button
var LED4 = new Gpio(19, 'out', { debounceTimeout: 10 }) //blinking blue button
var LED5 = new Gpio(13, 'out', { debounceTimeout: 10 }) //blinking blue button
var blinkInterval = setInterval(blinkLED, 200) //run the blinkLED function every 250ms
var blinkInterval2 = setInterval(blinkLED2, 450)

function blinkLED() {
  //function to start blinking
  if (LED4.readSync() === 0) {
    //check the pin state, if the state is 0 (or off)
    LED4.writeSync(1) //set pin state to 1 (turn LED on)
  } else {
    LED4.writeSync(0) //set pin state to 0 (turn LED off)
  }
}
function blinkLED2() {
  //function to start blinking
  if (LED5.readSync() === 0) {
    //check the pin state, if the state is 0 (or off)
    LED5.writeSync(1) //set pin state to 1 (turn LED on)
  } else {
    LED5.writeSync(0) //set pin state to 0 (turn LED off)
  }
}

function processMessage(dataKey, dataValue) {
  if (printer) {
    // LED1.writeSync(1)
    // LED2.writeSync(1)
    printer
      .printLine('')
      .printLine('')
      .center(true)
      .printImage(path)
      .bold(true)
      .printLine('BANK OF HYSTERIA')
      .bold(false)
      .printLine('')
      .printLine('Your emotion is valid.')
      .printLine('We hear you.')
      .printLine('')
      .center(false)
      .bold(true)
      .printLine('Deposit Details:')
      .bold(false)
      .printLine(dataValue)
      .printLine('')
      .center(true)
      .printLine('Thank you for investing with us.')
      .printLine('Call or text anytime at')
      .printLine('510-985-9986')
      .printLine('www.bohproject.org')
      .printLine('')
      .printLine('')
      .print()
    initializeBarGraph()
    blink()
  }
  console.log('data key: ', dataKey)
  console.log('data value: ', dataValue)
  console.log('number of messages in bank:', numMessages)
  //console.log('TEST number of messages in bank:', numMessagestest)
}

function blink() {
  // function turnOff() {
  //   //function to stop blinking
  //   LED1.writeSync(0) // Turn LED off
  //   LED2.writeSync(0)
  //   //LED1.unexport() // Unexport GPIO to free resources
  //   //LED2.unexport() // Unexport GPIO to free resources
  // }

  // setTimeout(turnOff, 25000)

  var blinkInterval3 = setInterval(blinkLED3, 500)
  var blinkInterval4 = setInterval(blinkLED4, 500)
  var blinkInterval5 = setInterval(blinkLED5, 500)

  function blinkLED3() {
    //function to start blinking
    if (LED3.readSync() === 0) {
      //check the pin state, if the state is 0 (or off)
      LED3.writeSync(1) //set pin state to 1 (turn LED on)
    } else {
      LED3.writeSync(0) //set pin state to 0 (turn LED off)
    }
  }

  function endBlink3() {
    //function to stop blinking
    clearInterval(blinkInterval3) // Stop blink intervals
    LED3.writeSync(0) // Turn LED off
    //LED3.unexport() // Unexport GPIO to free resources
  }

  setTimeout(endBlink3, 22000) //stop blinking after 5 seconds
  function blinkLED4() {
    //function to start blinking
    if (LED1.readSync() === 0) {
      //check the pin state, if the state is 0 (or off)
      LED1.writeSync(1) //set pin state to 1 (turn LED on)
    } else {
      LED1.writeSync(0) //set pin state to 0 (turn LED off)
    }
  }

  function endBlink4() {
    //function to stop blinking
    clearInterval(blinkInterval4) // Stop blink intervals
    LED1.writeSync(0) // Turn LED off
    //LED3.unexport() // Unexport GPIO to free resources
  }

  setTimeout(endBlink4, 22000) //stop blinking after 5 seconds
  function blinkLED5() {
    //function to start blinking
    if (LED2.readSync() === 0) {
      //check the pin state, if the state is 0 (or off)
      LED2.writeSync(1) //set pin state to 1 (turn LED on)
    } else {
      LED2.writeSync(0) //set pin state to 0 (turn LED off)
    }
  }

  function endBlink5() {
    //function to stop blinking
    clearInterval(blinkInterval5) // Stop blink intervals
    LED2.writeSync(0) // Turn LED off
    //LED3.unexport() // Unexport GPIO to free resources
  }

  setTimeout(endBlink5, 22000) //stop blinking after 5 seconds
}

function initializeBarGraph() {
  console.log('Count is: ', count)
  //needs to be continuously updating
  var PythonShell = require('python-shell')
  var options = {
    mode: 'text',
    pythonPath: 'python',
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: '/home/pi/boh_printer',
    args: [count]
  }

  var barScript = PythonShell.run(
    'bicolor_bargraph24_test.py',
    options,
    function(err, results) {
      if (err) throw err
      // results is an array consisting of messages collected during execution
      console.log('results: %j', results)
    }
  )
  barScript.terminate()
}
var count = 0
function initializeFirebase() {
  var firebase = require('firebase')
  var config = {
    apiKey,
    authDomain: 'bank-of-hysteria.firebaseapp.com',
    databaseURL: 'https://bank-of-hysteria.firebaseio.com',
    projectId: 'bank-of-hysteria',
    storageBucket: 'bank-of-hysteria.appspot.com',
    messagingSenderId
  }

  if (!firebase.apps.length) {
    firebase.initializeApp(config)
  }

  var database = firebase.database()
  var messages = firebase.database().ref('messages')
  var messageCount = firebase.database().ref('messageCount')
  //var count = 0;
  messages.once('value', function(snapshot) {
    initialDataLoaded = true
  })

  // length will always equal count, since snap.val() will include every child_added event
  // triggered before this point
  messages.once('value', function(snap) {
    console.log('initial data loaded!', snap.numChildren())
    count = snap.numChildren()
  })

  const debouncedProcessMessage = debounce(processMessage, 2000)
  messages.on('child_added', function(data) {
    if (initialDataLoaded) {
      count++
      debouncedProcessMessage(data.key, data.val())
    }
  })

  // numMessages is updated with the number of messages we have in total
  messageCount.on('value', function(data) {
    numMessages = data.val()
  })
}
//need to map numMessages to be inside (0,23)
//var numMessagestest = 10;

serialPort.on('open', function() {
  serialPort.flush(e => {
    printer = new Printer(serialPort)
    printer.on('ready', function() {
      initializeFirebase()
    })
  })
})

serialPort.on('error', () => {
  serialPort.close(() => console.log('Closed serial port.'))
  serialPort.flush(() => console.log('Serial port flushed.'))
})
