# text-normalizer

[![travis][travis-image]][travis-url]
[![pypi][pypi-image]][pypi-url]

[travis-image]: https://img.shields.io/travis/Yoctol/text-normalizer.svg?style=flat
[travis-url]: https://travis-ci.org/Yoctol/text-normalizer
[pypi-image]: https://img.shields.io/pypi/v/text-normalizer.svg?style=flat
[pypi-url]: https://pypi.python.org/pypi/text-normalizer

Normalize your Text String. 
It is a python package that help you normalize your text data and recover it.

## Install
Use Python3
```
> pip install text-normalizer
```
## Usage
```python
from text_normalizer.text_normalizer_collection_library import chinese_charactor_text_normalizer_collection_2


input_sentence = "   我在85.33度C買了一杯900──1000元的咖啡    《ohoh》？？ m_m"
nor_sentence, meta = chinese_charactor_text_normalizer_collection_2.normalize(input_sentence)
print(nor_sentence)
> "我在_float_度c買了一杯_int_-_int_元的咖啡 <ohoh>?? m_m"

de_sentence = chinese_charactor_text_normalizer_collection_2.denormalize(nor_sentence, meta)
print(de_sentence)
> "我在85.33度C買了一杯900──1000元的咖啡 《ohoh》？？ m_m",

```
