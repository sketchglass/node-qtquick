# node-qtquick

## Prerequisites

* Qt
* Node.js

## Setup

```
npm install # maybe fail at building native module but it's okay
```

## Build

```
node-gyp rebuild --qt_dir=/path/to/qt
# example: node-gyp rebuild --qt_dir=/Users/<username>/Qt/5.9/clang_64
```

## Test

```
npm test
```