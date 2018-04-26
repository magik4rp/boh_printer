const { apiKey, messagingSenderId } = require('./constants')
var moment = require('moment')
var SerialPort = require('serialport'),
  serialPort = new SerialPort('/dev/serial0', {
    baudRate: 19200
  }),
  Printer = require('thermalprinter')

var path = __dirname + '/images/boh.jpg'
var printer, numMessages

function processMessage(dataKey, dataValue) {
  if (printer) {
    printer
      .printLine('')
      .printLine('')
      .center(true)
      .printImage(path)
      .bold(true)
      .printLine('BANK OF HYSTERIA')
      .bold(false)
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
      .printLine('')
      .printLine('')
      .print()
  }
  console.log('data key: ', dataKey)
  console.log('data value: ', dataValue)
}

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
  firebase.initializeApp(config)
  var database = firebase.database()
  var messages = firebase.database().ref('messages')
  var messageCount = firebase.database().ref('messageCount')

  messages.on('child_added', function(data) {
    processMessage(data.key, data.val())
  })

  // numMessages is updated with the number of messages we have in total
  messageCount.on('value', function(data) {
    numMessages = data.val()
  })
}

serialPort.on('open', function() {
  printer = new Printer(serialPort)
  printer.on('ready', function() {
    initializeFirebase()
  })
})

initializeFirebase()
