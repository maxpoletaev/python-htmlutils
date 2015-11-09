from htmlutils import parse_attrs, render_attrs, render_tag, tags
from collections import OrderedDict
from unittest import TestCase


class TestHtml(TestCase):
    def test_parse_attrs(self):
        test_str = 'color="red" edit font-size="12" required'
        expect = dict(color='red', font_size='12', required=True, edit=True)
        self.assertDictEqual(parse_attrs(test_str), expect)

    def test_render_attrs(self):
        attrs = OrderedDict()
        attrs['color'] = 'red'
        attrs['font_size'] = '12'
        attrs['required'] = True
        attrs['edit'] = True

        result = render_attrs(attrs)
        expect = 'color="red" font-size="12" required edit'
        self.assertEqual(result, expect)

    def test_render_tag(self):
        self.assertEqual(
            render_tag('input', required=True, _xhtml=True, _single=True),
            '<input required="required" />',
        )
        self.assertEqual(
            tags.h1('hello', _class='heading'),
            '<h1 class="heading">hello</h1>',
        )
        self.assertEqual(tags.input(required=True), '<input required>')
