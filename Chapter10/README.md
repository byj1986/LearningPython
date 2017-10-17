## This project introduces base modules from python

### Markdown language

Head
====

Head2
----

Head3
****


#### Title
    # for level 1 title
    ## for level 2 title
    ### for level 3 title
    ...

#### Ordered list
1. for ordered list



#### Disordered list
* 1 disordered list
+ 2 disordered list
- 3 disordered list

#### Reference
> Reference sample
> Reference sample2


#### Hyper-link
[Baidu](http://www.baidu.com)
<http://cn.bing.com>
#### Image
![Mou icon](http://mouapp.com/Mou_128.png)

#### Bold text
1. **Bold**: The Quick Brown **Fox** Jumps Over the Lazy **Dog**
2. *Italic*: The Quick Brown *Fox* Jumps Over the Lazy *Dog*
3. ***Bold&Italic***: The Quick Brown ***Fox*** Jumps Over the Lazy ***Dog***

#### Code
    static void main(string[] args)
    {
        System.Console.WriteLine("Hello World");
    }

    def g(x):
        yield from range(x, 0, -1)
    yield from range(x)

    ```nohighlight
    ```

#### Code2
    ```python
       @requires_authorization
       def somefunc(param1='', param2=0)
           '''a dogstring'''
           if param1 > param2: # interesting
               print 'Greater'
           return (param2 - param1 +1) or None
       class SomeClass:
           pass
    ```