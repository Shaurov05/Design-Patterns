# Design Patterns

Design patterns are design level concept for recurring real world problems that we usually come across. Its not **code**. I repeat, ❌ (not) CODE!
It is a concept of how we design a solution to tackle these problems.

Before going further I want to talk about something else.
- **Idioms:** Idioms or low-level patterns in software development refer to commonly used coding patterns or practices that are considered efficient, expressive, or "the right way" to do things in a particular programming language or environment. 
  - **Examples:** of idioms include using list comprehensions in Python, using the "using" statement for resource management in C#, or using functional programming constructs like map and filter in functional languages.
- **Anti-patterns:** Anti-patterns are common practices that appear to be solutions to problems but are counterproductive or lead to poor outcomes.
  - **Examples** of anti-patterns include the "God Object" anti-pattern, where a single class or module takes on too many responsibilities, making the codebase hard to maintain and understand. Another example is the "Spaghetti Code" anti-pattern, where code is tangled and lacks proper structure or organization, making it difficult to follow or modify.

The single biggest benefit of design patterns is that it gives developers a common vocabulary to talk about software solutions.
If I say, "We should implement this using the singleton pattern", we have a common point of reference to begin discussing whether that is a good idea without me having to actually implement the solution first or not, so you know what I mean.

It adds readability and maintainability that comes with familiar solutions to common problems, instead of every developer trying to solve the problem in their own way over an over again.

**Pretty important:** Software can be made without them, but it's certainly a lot harder.

**The good**

  - **Code readability:** They do help you write more understandable code with better names for what you are trying to accomplish.
  - **Code maintainability:** Allows your code to be maintained easier because it is more understandable.
  - **Communication:** They help you communicate design goals amongst programmers.
  - **Intention:** They show the intent of your code instantly to someone learning the code.
  - **Code re-use:** They help you identify common solutions to common problems.
  - **Less code:** They allow you to write less code because more of your code can derive common functionality from common base classes.
  - **Tested and sound solutions:** Most of the design patterns are tested, proven and sound.

**The bad**

  * **Extra levels of indirection:** They provide an extra level of indirection and hence make the code a little more complex.
  * **Knowing when to use them:** They are often abused and used in cases that they should not be. A simple task may not need the extra work of being solved using a design pattern.
  * **Different interpretations:** People sometimes have slightly different interpretations of design patterns. Example MVC as seen by django vs. MVC as seen by Ruby on Rails.
  * **Unjustified use:** The problem that haunts many developers who have just familiarized themselves with patterns. Having learned about patterns, they try to apply them everywhere, even in situations where simpler code would do just fine.
>If all you have is a hammer, everything looks like a nail.


One quote can be recalled for this scenario:
> The purpose of software engineering is to control complexity, not to create it. 
>> _-Pamela Zave_

### Classification of patterns
Design patterns differ by their complexity, level of detail and scale of applicability to the entire system being designed. 
The most basic and low-level patterns are often called idioms. They usually apply only to a single programming language.

The most universal and high-level patterns are architectural patterns. 
In addition, all patterns can be categorized by their intent, or purpose. This book covers three main groups of patterns:

* **Creational patterns** provide object creation mechanisms that increase flexibility and reuse of existing code.
* **Structural patterns** explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.
* **Behavioral patterns** take care of effective communication and the assignment of responsibilities between objects.


