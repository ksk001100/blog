+++
title = "RubyのHashとArrayの文字列要素をforce_encoding"
date = 2019-12-24
weight = 1

[taxonomies]
tags = ["Ruby"]
+++

RubyのHashとArrayの文字列要素を再帰的に`force_encoding`する

```ruby
def encoding_hash(hash, encode = Encoding::UTF_8)
  hash&.map do |k, v|
    case v
    when Hash then [k, encoding_hash(v, encode)]
    when Array then [k, encoding_array(v, encode)]
    when String then [k, v.force_encoding(encode)]
    else [k, v]
    end
  end&.to_h
end

def encoding_array(array, encode = Encoding::UTF_8)
  array&.map do |v|
    case v
    when Hash then encoding_hash(v, encode)
    when Array then encoding_array(v, encode)
    when String then v.force_encoding(encode)
    else v
    end
  end
end	
```

もしくは関数にするよりオープンクラスにしたほうがいいかもしれない

```ruby
class Hash
  def encoding(encode = Encoding::UTF_8)
    self&.map do |k, v|
      case v
      when Hash, Array then [k, v.encoding(encode)]
      when String then [k, v.force_encoding(encode)]
      else [k, v]
      end
    end&.to_h
  end
end

class Array
  def encoding(encode = Encoding::UTF_8)
    self&.map do |v|
      case v
      when Hash, Array then v.encoding(encode)
      when String then v.force_encoding(encode)
      else v
      end
    end
  end
end
```