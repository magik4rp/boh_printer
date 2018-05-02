'use strict'

const percent = require('cpu-percent')
const j5 = require('johnny-five')
const raspi = require('raspi-io')
const bargraph = require('bicolor-bargraph')

function color(i) {
  if (i > 16) {
    return bargraph.GREEN
  } else if (i > 8) {
    return bargraph.YELLOW
  }
  return bargraph.RED
}

function initializeBarGraph() {
  new j5.Board({
    io: new raspi(),
    repl: false
  }).on('ready', () => {
    const bar = bargraph()
    percent((err, value) => {
      if (err) {
        throw err
      }
      // invert numbers to change "direction"
      const pct = Math.round(24 * (100 - value) / 100)
      const [cols, values] = [[], []]
      for (let i = 0; i < 24; i++) {
        cols.push(i)
        values.push(pct <= i ? color(i) : bargraph.OFF)
      }
      // sets many LEDs at once in a single I2C write
      bar.leds(cols, values)
    })
  })
}

module.exports = initializeBarGraph
