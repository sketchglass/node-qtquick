const assert = require('assert')
const lib = require('../lib')

describe('node-qtquick', () => {
  describe('hello', () => {
    it('returns string via QString', () => {
      assert(lib.hello() === 'world')
    })
  })
})
