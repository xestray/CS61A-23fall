test = {
  'name': 'Lists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [7//3, 5, [4, 0, 1], 2]
          >>> s[0]
          61b793952531daad90d65377b695da99
          # locked
          >>> s[2]
          176f11e2ea330c098313db1f1576967f
          # locked
          >>> s[-1]
          61b793952531daad90d65377b695da99
          # locked
          >>> len(s)
          e6efc1fcfbebed28c5068a807b6cce64
          # locked
          >>> 4 in s
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 4 in s[2]
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> s + [3 + 2, 9]
          5fa369a12d6e829ddd23df6bae5d8cf3
          # locked
          >>> s[2] * 2
          2ada3a8823635a1d6945f06fab16565d
          # locked
          >>> x = [1, 2, 3, 4]
          >>> x[1:3]
          d9f2f79c63bb0452cca111f0097f6e01
          # locked
          >>> x[:2]
          85f4791dbde2a41b1fd5129362586cda
          # locked
          >>> x[1:]
          0b59790ac79a2cfefac6e5d199a6af1b
          # locked
          >>> x[-2:3]
          10d6d3f2082a5022fbec819887cd9320
          # locked
          >>> x[-2:4]
          4105fdd22b14e14231ca9721a4f4d0a6
          # locked
          >>> x[0:4:2]
          a2ac037792793d9a90a21125289c4193
          # locked
          >>> x[::-1]
          195dddf24581be91800af2053bec3f39
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
