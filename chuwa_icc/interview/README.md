# Design patterns 
[Singleton](#singleton)

[Other patterns]

# Spring 
[IC and IOC](#ic-and-ioc)

[Scope]

[Bean]

[Annotations]


# Java basic 

 
# Database 

# Software life cycle 




## Singleton


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


