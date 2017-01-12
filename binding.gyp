{
  "targets": [
    {
      "target_name": "qtquick",
      "sources": [ "src/qtquick.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-std=c++11 -stdlib=libc++',
              '-mmacosx-version-min=10.7'
            ],
          },
          'include_dirs': [
            '<(qt_dir)/lib/QtCore.framework/Headers',
            '<(qt_dir)/lib/QtGui.framework/Headers',
            '<(qt_dir)/lib/QtQml.framework/Headers',
          ],
          'link_settings': {
            'libraries': [
              '<(qt_dir)/lib/QtCore.framework',
              '<(qt_dir)/lib/QtGui.framework',
              '<(qt_dir)/lib/QtQml.framework',
            ],
            'mac_framework_dirs': [
              '<(qt_dir)/lib',
            ],
          },
        }]
      ]
    }
  ]
}
