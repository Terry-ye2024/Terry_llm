# Terry_llm

# reference
NanoGPT

# Introduction
Learning NanoGPT and doing a simple exercise

# Requirements
1.Tiktoken

2.numpy

3.pytorch>=2.0

# Log
## 10.21
·Finished the model structure

·learing Embedding function

·colecting datasets and learning encoding and decoding
## 10.22
· 选择了sherlock作为datasets

· 采用cl100k_base作为编码方式，比gpt2处理效率更高

· 由于内存不够（out of bounds）故还是采用gpt2

## 10.26
·尝试 dill 模块：dill 是一种 pickle 的扩展，可以序列化更多的 Python 对象。安装 dill 后，尝试用它来加载模型：成功

·尝试引入自注意力机制：失败，由于维度不匹配产生了NAN

##10.27
· 尝试在GPU上运行代码，成功生成完整的sherlock对话
