# Design patterns 
[Singleton](#singleton)

[Other patterns]

# Spring 
[IOC and DI](#ioc-and-di)

[Scope]

[Bean]

[Annotations]


# Java basic 

 
# Database 

# Software life cycle 




## Singleton
### lazy loading thread safe 
```java
package pattern.singleton.demo5;
/*
double checked locking

Despite this class being thread-safe, we can see that there's a clear performance drawback: each time we want to get the instance of our singleton, we need to acquire a potentially unnecessary lock.

To fix that, we could instead start by verifying if we need to create the object in the first place and only in that case we would acquire the lock.
 */
public class Singleton {

    private Singleton(){}

    private static Singleton instance;

    public static Singleton getInstance(){

        //第一次判断，如果instance不为null，不进入抢锁阶段，直接返回实际
        if (instance==null){
            synchronized (Singleton.class){
                //抢到锁之后再次判断是否为空
                if (instance==null){
                    instance=new Singleton();
                }
            }
        }

        return instance;
    }
}

```

To check 

```java
package pattern.singleton.demo5;


import pattern.singleton.demo5.Singleton;

public class Client {

    public static void main(String[] args){

        pattern.singleton.demo5.Singleton instance1= Singleton.getInstance();

        pattern.singleton.demo5.Singleton instance2= Singleton.getInstance();

        System.out.println(instance1==instance2);

    }

}
```
### how to break singleton 
https://www.geeksforgeeks.org/prevent-singleton-pattern-reflection-serialization-cloning/

### reflection  Reflection can be caused to destroy singleton property of singleton class, as shown in following example:
Overcome reflection issue: To overcome issue raised by reflection, enums are used because java ensures internally that enum value is instantiated only once. Since java Enums are globally accessible, they can be used for singletons. Its only drawback is that it is not flexible i.e it does not allow lazy initialization.
As enums don’t have any constructor so it is not possible for Reflection to utilize it. Enums have their by-default constructor, we can’t invoke them by ourself. JVM handles the creation and invocation of enum constructors internally. As enums don’t give their constructor definition to the program, it is not possible for us to access them by Reflection also. Hence, reflection can’t break singleton property in case of enums.

### serialization:  Serialization can also cause breakage of singleton property of singleton classes. Serialization is used to convert an object of byte stream and save in a file or send over a network. Suppose you serialize an object of a singleton class. Then if you de-serialize that object it will create a new instance and hence break the singleton pattern.
To overcome this issue, we have to implement method readResolve() method.


### cloning: Cloning is a concept to create duplicate objects. Using clone we can create copy of object. Suppose, we create clone of a singleton object, then it will create a copy that is there are two instances of a singleton class, hence the class is no more singleton.
To overcome this issue, override clone() method and throw an exception from clone method that is CloneNotSupportedException. Now whenever user will try to create clone of singleton object, it will throw exception and hence our class remains singleton.


## IOC and DI
https://www.baeldung.com/inversion-control-and-dependency-injection-in-spring

Inversion of Control is a principle in software engineering which transfers the control of objects or portions of a program to a container or framework. We most often use it in the context of object-oriented programming.

In contrast with traditional programming, in which our custom code makes calls to a library, IoC enables a framework to take control of the flow of a program and make calls to our custom code. To enable this, frameworks use abstractions with additional behavior built in. If we want to add our own behavior, we need to extend the classes of the framework or plugin our own classes.

The advantages of this architecture are:

- decoupling the execution of a task from its implementation
- making it easier to switch between different implementations
- greater modularity of a program
- greater ease in testing a program by isolating a component or mocking its dependencies, and allowing components to communicate through contracts

We can achieve Inversion of Control through various mechanisms such as: Strategy design pattern, Service Locator pattern, Factory pattern, and Dependency Injection (DI).

What is DI?

https://stackoverflow.com/questions/130794/what-is-dependency-injection

Dependency injection is basically providing the objects that an object needs (its dependencies) instead of having it construct them itself. It's a very useful technique for testing, since it allows dependencies to be mocked or stubbed out.

Dependencies can be injected into objects by many means (such as constructor injection or setter injection). One can even use specialized dependency injection frameworks (e.g. Spring) to do that, but they certainly aren't required. You don't need those frameworks to have dependency injection. Instantiating and passing objects (dependencies) explicitly is just as good an injection as injection by framework.

Three ways of using DI in spring, which one is better or best practise?

https://dzone.com/articles/best-practices-for-dependency-injection-with-sprin




## Scope 


## Bean 
## Annotations 


