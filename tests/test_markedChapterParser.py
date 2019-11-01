from unittest import TestCase


class TestMarkedChapterParser(TestCase):
    def test_parse(self):
        text = \
            """
            * chapter 1
                - [Sub Chapter 1](/go1)
                - Subchapter 2 whithout link
                    * sub under sub 2
                    * another sub under sub 2
            - [Chapter 2](/ch2)
            - Ch 1 Pt 2
    
            1. ch p none
                - sub ch p none
                    - more sub ch p none
            - And this
    
            """
        p = MarkedChapterParser(None, text)
        toc = p.parse()
        print()
        # for p in toc.parts:
        #     print(p)
        print(toc.as_html(added_level=1))

