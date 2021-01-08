





![image-20191228223912033](/Users/jw/Library/Application Support/typora-user-images/image-20191228223912033.png)

![image-20191228225513026](/Users/jw/Library/Application Support/typora-user-images/image-20191228225513026.png)



Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. This is known as aliasing in other languages. This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples). **However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types.**

동일한 이름의 객체에 여러 이름, 여러 scope가 적용될 수 있다.

![image-20191228230844280](/Users/jw/Library/Application Support/typora-user-images/image-20191228230844280.png)

특수한 효과가 뭐지..?

![image-20191228231031560](/Users/jw/Library/Application Support/typora-user-images/image-20191228231031560.png)



![image-20191228231204639](/Users/jw/Library/Application Support/typora-user-images/image-20191228231204639.png)

![image-20191228231325460](/Users/jw/Library/Application Support/typora-user-images/image-20191228231325460.png)

![image-20191228231414710](/Users/jw/Library/Application Support/typora-user-images/image-20191228231414710.png)

![image-20191228231437163](/Users/jw/Library/Application Support/typora-user-images/image-20191228231437163.png)

![image-20191228231455444](/Users/jw/Library/Application Support/typora-user-images/image-20191228231455444.png)

![image-20191228231703712](/Users/jw/Library/Application Support/typora-user-images/image-20191228231703712.png)

만약 if를 돌면서 immutable 객체의 값을 바꾸는 코드가 있다고 하자.그럼 객체가 계속 생겨나서, 메모리 때문에 코드가 실행이 되지 않는 경우가 생긴다. 반대로 mutable 객체에 값을 넣고, 다 사용한 후에 삭제를 하지 않거나 garbage collecting 대상으로 하지 않으면 계속 메모리에 상주하는 경우가 생긴다.

효율적으로 메모리를 잘 관리하게 짜려면 이 개념을 잘 알아둬야 한다.

## Class vs Instance

![image-20191228232556452](/Users/jw/Library/Application Support/typora-user-images/image-20191228232556452.png)

![image-20191228232815140](/Users/jw/Library/Application Support/typora-user-images/image-20191228232815140.png)

![image-20191228232859026](/Users/jw/Library/Application Support/typora-user-images/image-20191228232859026.png)

![image-20191228232952816](/Users/jw/Library/Application Support/typora-user-images/image-20191228232952816.png)



![image-20191228233559385](/Users/jw/Library/Application Support/typora-user-images/image-20191228233559385.png)

![image-20191228233704904](/Users/jw/Library/Application Support/typora-user-images/image-20191228233704904.png)

![image-20191228233727182](/Users/jw/Library/Application Support/typora-user-images/image-20191228233727182.png)

![image-20191228233536510](/Users/jw/Library/Application Support/typora-user-images/image-20191228233536510.png)

![image-20191228233819047](/Users/jw/Library/Application Support/typora-user-images/image-20191228233819047.png)





![image-20191228233914120](/Users/jw/Library/Application Support/typora-user-images/image-20191228233914120.png)

![image-20191228234001366](/Users/jw/Library/Application Support/typora-user-images/image-20191228234001366.png)



![image-20191228234044246](/Users/jw/Library/Application Support/typora-user-images/image-20191228234044246.png)

변하지 않아야 되는 값이라면, 클래스 변수로 만들고 변수명에서 바꾸지 말라는 표시를 해준다.

그리고 사용할 때도 self말고 클래스 이름으로 호출해준다.

![image-20191228234830628](/Users/jw/Library/Application Support/typora-user-images/image-20191228234830628.png)



![image-20191228235032669](/Users/jw/Library/Application Support/typora-user-images/image-20191228235032669.png)

![image-20191228235203996](/Users/jw/Library/Application Support/typora-user-images/image-20191228235203996.png)

![image-20191228235434004](/Users/jw/Library/Application Support/typora-user-images/image-20191228235434004.png)

![image-20191228235509723](/Users/jw/Library/Application Support/typora-user-images/image-20191228235509723.png)



![image-20191228235607337](/Users/jw/Library/Application Support/typora-user-images/image-20191228235607337.png)

![image-20191228235711999](/Users/jw/Library/Application Support/typora-user-images/image-20191228235711999.png)

![image-20191228235758532](/Users/jw/Library/Application Support/typora-user-images/image-20191228235758532.png)