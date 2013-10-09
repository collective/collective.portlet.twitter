There's a frood who really knows where his towel is
---------------------------------------------------

1.0b4 (unreleased)
^^^^^^^^^^^^^^^^^^

- Nothing changed yet.


1.0b3 (2013-10-09)
^^^^^^^^^^^^^^^^^^

- Fix package distribution; we are not including anymore the screenshots used
  in the documentation reducing significatively the egg size.
  [hvelarde]

- Fix potential XSS (arbitrary injection) issue by escaping and quoting all
  attributes being set on the rendered portlet.
  [davidjb]


1.0b2 (2013-06-28)
^^^^^^^^^^^^^^^^^^

- Fix specifying the ``data-related`` attribute without a value.
  [davidjb]
- Add ability to customise portlet header text and ability to show just the
  Twitter widget (omit border).
  [davidjb]
- Link portlet title to the user's Twitter timeline.
  [davidjb]
- Update descriptions for Twitter client configuration to be end-user
  readable and add examples.
  [davidjb]
- Add ``tweet-limit`` client-side configuration option to control the number
  of tweets displayed.
  [davidjb]
- Add titles and descriptions to the portlet add and edit pages.
  [davidjb]
- Remove tal:attributes specification from Twitter link in portlet page 
  template. This is already handled by the HTML tag creation code, and lead
  to rendering failure in some cases (see 
  https://bugs.launchpad.net/zope2/+bug/1004588).
  [davidjb]


1.0b1 (2013-04-24)
^^^^^^^^^^^^^^^^^^

- Initial release.
