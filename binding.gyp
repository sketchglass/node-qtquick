{
  "targets": [
    {
      "target_name": "qtquick",
      "sources": [ "src/qtquick.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
