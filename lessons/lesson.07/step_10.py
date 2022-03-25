import sys

import numpy


def convert_to_pdf(src):
    import pdf_converter

    a = numpy.sin(2)

    result = pdf_converter.convert(src)
    return result


