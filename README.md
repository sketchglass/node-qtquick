# node-qtquick

[WIP] Use Qt Quick from Node.js

- Create Qt Quick app with Node.js, without writing C++
- Access C++ code from JavaScript easily through Qt plugin

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

## TODO

- [ ] Load Qt object through QPluginLoader
- [ ] Invoke method/setter/getter from Node.js through meta object
- [ ] Provide API for creating Qt Quick app from Node.js