# FuncMage — Complete Conceptual Review

_This project has been created as part of the 42 curriculum by mahendri._

---

## Exercise 0 — Lambda & Functional Builtins

### Lambda expressions

**What is a lambda expression? How does it differ from a `def` function?**
```
A lambda is an anonymous, single-expression function. `def` creates a named function and supports multiple statements, loops, and assignments. Lambda supports exactly one expression and returns it implicitly.
```

**What are the syntactic limitations of lambda?**
```
Single expression only. No statements, no assignments, no `return`, no `for` loops, no `if/else` blocks (only ternary allowed).
```

**What is the ternary expression and how does it work inside a lambda?**
```
`lambda x: x if x > 0 else -x` — evaluates the condition and returns one of two expressions. This is the only branching allowed in a lambda.
```

**When should you use lambda vs `def`? What does PEP8 say?**
```
Use lambda for short, one-time, throwaway operations passed as arguments (e.g. `key=` in `sorted`). PEP8 says never assign a lambda to a variable — use `def` instead. If the logic needs a name, use `def`.
```

---

### map / filter / sorted

**What does `map()` return?**
```
A lazy iterator (`map` object), not a list. You must call `list()` on it to materialize results.
```

**What does `filter()` return?**
```
Same — a lazy iterator (`filter` object). Convert with `list()`.
```

**Why does Python use lazy iterators instead of returning lists?**
```
Memory efficiency. A lazy iterator computes values one at a time on demand, instead of building the entire result in memory upfront.
```

**Difference between `sorted()` and `.sort()`?**
```
`sorted()` takes any iterable and returns a **new** list — the original is unchanged (functional style). `.sort()` mutates the list in place and returns `None`.
```

**How does the `key` parameter work in `sorted()`?**
```
It accepts a callable. `sorted()` calls it on each element and sorts by the returned value. The original elements are returned in the result, not the key values.
```

**What is a stable sort? What algorithm does Python use?**
```
A stable sort preserves the original order of elements that compare equal. Python uses **Timsort** — always stable, O(n log n).
```

---

### Functional purity concepts

**What is a pure function?**
```
A function that: always returns the same output for the same input, and has no side effects.
```

**What is a side effect? Give 3 examples.**
Any observable change outside the function's return value. Examples: printing to stdout, modifying a global variable, writing to a file.

**What is immutability?**
```
Data that cannot be changed after creation. Functional programming favors immutability to avoid shared mutable state and side effects.
```

**Why are `map/filter` more functional than `for` loops?**
```
They express *what* to compute, not *how*. They do not mutate the input collection and produce new values without side effects — closer to mathematical functions.
```

---

## Exercise 1 — Higher-Order Functions

### First-class functions

**What does "first-class citizen" mean in Python?**
```
Functions can be assigned to variables, passed as arguments, returned from functions, and stored in data structures — exactly like integers or strings.
```

**Difference between calling `f()` and passing `f`?**
```
`f()` executes the function and returns its result. `f` is a reference to the function object itself, which can be stored or passed without executing.
```

**Can you store functions in a list or dict?**
```
Yes. `[fireball, heal, shield]` and `{'attack': fireball, 'heal': heal}` are both valid.
```

---

### Higher-order functions

**What is a higher-order function?**
```
A function that takes one or more functions as arguments, or returns a function as its result, or both.
```

**Is `map()` a higher-order function? Is `sorted()`?**
```
Yes to both. `map(func, iterable)` takes a function. `sorted(iterable, key=func)` takes a function as `key`.
```

**What is function composition?**
```
Combining two or more functions so the output of one becomes the input of the next. `spell_combiner` calls both functions on the same input — that is parallel application, not strict composition. True composition: `f(g(x))`.
```

---

### `Callable` and `callable()`

**Why use `collections.abc.Callable` instead of `typing.Callable`?**
```
`collections.abc.Callable` is the real Abstract Base Class. `typing.Callable` was a wrapper around it, deprecated since Python 3.9. Using `collections.abc` directly is the current standard.
```

**What does `callable(obj)` do?**
```
Returns `True` if the object can be called (has a `__call__` method). Works at runtime, unlike type hints.
```

**What is `__call__`?**
```
A special method that makes a class instance callable. If a class defines `__call__`, its instances can be used as functions: `obj(args)`.
```

---

### Closures in higher-order functions

**When `power_amplifier` returns `amplifier`, what does `amplifier` close over?**
```
It closes over `base_spell` and `multiplier` — the variables from the enclosing scope of `power_amplifier`.
```

**What is a free variable?**
```
A variable used inside a function but not defined there — it comes from the enclosing scope. `multiplier` is a free variable inside `amplifier`.
```

**What happens to `multiplier` after `power_amplifier` returns?**
```
It is kept alive by the closure. The garbage collector cannot collect it because `amplifier` holds a reference to it via its `__closure__`.
```

---

## Exercise 2 — Closures & Lexical Scoping

### LEGB scoping rules

**What does LEGB stand for?**
```
Local → Enclosing → Global → Built-in. Python resolves names in this order.
```

**What is the difference between local, enclosing, global, and built-in scope?**
```
- Local: inside the current function.
- Enclosing: in outer (non-global) functions that contain the current function.
- Global: module level.
- Built-in: Python's built-in names (`len`, `print`, `range`, etc.).
```

**What happens if the same name exists in two scopes?**
```
The innermost scope wins. Local shadows enclosing, enclosing shadows global.
```

---

### Closures

**What is a closure? Precise definition.**
A closure is a function that captures and retains references to variables from its enclosing lexical scope, even after that scope has finished executing.

**What are the 3 conditions for a closure to exist?**
```
1. There is a nested function.
2. The nested function refers to a variable from the enclosing function.
3. The enclosing function returns the nested function.
```

**How do you inspect a closure?**
```
`func.__closure__` returns a tuple of cell objects. `func.__code__.co_freevars` returns the names of the captured variables.
```

**Can a closure close over a mutable object?**
```
Yes. The closure holds a reference to the object. Mutations to that object (e.g. `list.append`) are visible across all references. Rebinding the name requires `nonlocal`.
```

---

### `nonlocal` vs `global`

**What does `nonlocal` do?**
```
Declares that a variable name refers to the nearest enclosing scope (not global). Allows reassignment of that variable from inside an inner function.
```

**What does `global` do?**
```
Declares that a variable name refers to the module-level global scope, allowing assignment to it from inside a function.
```

**Why is `global` an anti-pattern in functional programming?**
```
Global variables are shared mutable state. Any function can read or modify them, making behavior unpredictable, testing hard, and reasoning about correctness difficult.
```

**Why is `nonlocal` less harmful than `global`?**
```
`nonlocal` only reaches the immediately enclosing function scope — the state is contained, private, and scoped to that closure. It does not pollute the module.
```

**What error do you get if you assign to an enclosing variable without `nonlocal`?**
```
`UnboundLocalError: local variable 'x' referenced before assignment`. Python sees the assignment and treats the variable as local, then fails when it is read before being assigned.
```

**Why does mutating a dict not require `nonlocal` but reassigning an int does?**
```
`d['key'] = value` calls a method on the existing object — the variable `d` is never rebound. `x += 1` is `x = x + 1` — it rebinds the name `x`, which requires `nonlocal`.
```

---

### State in closures

**Difference between mutating a variable and rebinding it?**
```
Mutating: modifying the object a variable points to (`list.append`, `dict['k'] = v`). Rebinding: making the variable point to a different object (`x = x + 1`, `x = []`). Only rebinding requires `nonlocal`.
```

**The classic late-binding closure bug:**
```python
funcs = [lambda: i for i in range(3)]
funcs[0]()  # returns 2, not 0
```
All three lambdas close over the same `i` variable. By the time they are called, the loop has finished and `i` is `2`. Fix: `lambda i=i: i` — captures the current value as a default argument.

---

## Exercise 3 — functools

### `functools.reduce`

**What is reduce conceptually?**
```
It takes a binary function and a sequence, applies the function cumulatively from left to right, reducing the sequence to a single value.
```

**What are its arguments?**
```
`reduce(function, iterable[, initializer])`. The function takes two arguments: accumulator and current element.
```

**What happens with an empty list and no initializer?**
```
`TypeError: reduce() of empty iterable with no initial value`.
```

**What happens with a single-element list?**
```
Returns that element directly. The function is never called.
```

**What is left fold vs right fold? Which is `reduce`?**
```
Left fold: processes left to right, `f(f(f(a, b), c), d)`. Right fold: right to left. `functools.reduce` is a left fold.
```

---

### `functools.partial`

**What is partial application?**
```
Fixing some arguments of a function to produce a new function with fewer parameters.
```

**What does `functools.partial` return?**
```
A `partial` object — callable, with attributes `.func`, `.args`, `.keywords` showing what was pre-filled.
```

**Difference between partial application and currying?**
```
Currying transforms `f(a, b, c)` into `f(a)(b)(c)` — one argument at a time, always returns a unary function. Partial application fixes any number of arguments at once, returning a function with fewer parameters.
```

---

### `functools.lru_cache`

**What is memoization?**
```
Caching the return value of a function for given inputs so repeated calls with the same arguments return the cached result without recomputation.
```

**What does LRU stand for?**
```
Least Recently Used — the eviction policy when the cache is full.
```

**What does `maxsize=None` do?**
```
Disables the size limit. The cache grows unboundedly. Equivalent to `@functools.cache` (Python 3.9+).
```

**Why must arguments be hashable?**
```
Cache keys are built from the arguments. Only hashable objects can be used as dict keys.
```

**What does `.cache_info()` return?**
```
A named tuple: `CacheInfo(hits, misses, maxsize, currsize)`. Hits = served from cache. Misses = computed and cached.
```

**Time complexity of fibonacci with vs without cache?**
```
Without: O(2^n) — exponential. With `lru_cache`: O(n) — each value computed once.
```

---

### `functools.singledispatch`

**What problem does it solve?**
```
Allows one function name to dispatch to different implementations based on the type of the first argument, without `isinstance` chains.
```

**What is the Open/Closed Principle here?**
```
Open for extension (add new type handlers without modifying existing code), closed for modification (the dispatch logic does not change when new types are added).
```

**How do you register a handler?**
```
Two syntaxes:
```
```python
@func.register(int)
def _(x): ...

# or with annotation (Python 3.7+)
@func.register
def _(x: int): ...
```

**What happens when no handler matches?**
```
Falls back to the base function (decorated with `@singledispatch`), registered under `object`.
```

**Why does `bool` dispatch to `int` handler?**
```
`bool` is a subclass of `int` in Python. singledispatch walks the MRO — if no `bool` handler exists, it finds the `int` handler.
```

**What is `func.dispatch(type)`?**
```
Returns the implementation that would be called for the given type — useful for inspection and debugging.
```

---

### `functools.wraps`

**What attributes does it copy?**
```
`__name__`, `__qualname__`, `__doc__`, `__module__`, `__annotations__`, `__dict__`, and sets `__wrapped__` to the original function.
```

**What is `__wrapped__`?**
```
A reference to the original unwrapped function. Allows introspection tools and `inspect.unwrap()` to bypass decorators.
```

**What breaks without `functools.wraps`?**
```
`func.__name__` returns `"wrapper"` instead of the original name. `help(func)` shows the wrapper docstring. Stacked decorators lose the chain. Debugging and logging show wrong names.
```

---

## Exercise 4 — Decorators & Class Methods

### Decorator fundamentals

**What is the `@` syntax sugar for?**
```python
@decorator
def func(): ...
# is exactly:
func = decorator(func)
```

**What does a decorator receive and return?**
```
Receives: a callable (the decorated function). Returns: a callable (the wrapper that replaces it).
```

**Difference between a decorator and a decorator factory?**
```
A decorator takes a function directly. A decorator factory takes configuration parameters and returns a decorator, which then takes the function. One extra level of nesting.
```

**Stacking decorators — what order do they apply?**
```python
@a
@b
def f(): ...
# equivalent to: f = a(b(f))
# b wraps f first, then a wraps the result
# when f() is called: a's wrapper runs first, then b's
```

---

### `*args` and `**kwargs` in wrappers

**Why do wrappers use `*args, **kwargs`?**
```
To be transparent — the wrapper forwards all arguments to the original function without knowing or hardcoding its signature. This makes the decorator reusable for any function.
```

**Risk of explicit parameters in a wrapper?**
```
The decorator only works for functions with that exact signature. It breaks for any other function.
```

---

### `@staticmethod`

**Difference between `@staticmethod`, `@classmethod`, and instance method?**
```
- Instance method: receives `self` — access to instance and class.
- Class method: receives `cls` — access to class only, not instance.
- Static method: receives nothing implicit — just a regular function namespaced in the class.
```

**How is a static method called?**
```
Both `MyClass.method(args)` and `instance.method(args)` work. No instance is required.
```

**When to use `@staticmethod` vs a module-level function?**
```
When the function is logically related to the class but does not need access to instance or class state. It communicates intent and keeps related code together.
```

**What is a descriptor? How does `staticmethod` use it?**
```
A descriptor is an object that defines `__get__`, `__set__`, or `__delete__`. `staticmethod` is a descriptor — when accessed through the class or instance, its `__get__` returns the raw underlying function without binding `self` or `cls`.
```
---

### `@classmethod`

**What is `cls`? What can you do with it?**
```
`cls` is the class itself (not an instance). You can call `cls(...)` to create instances, access class-level attributes, and call other class methods — useful for alternative constructors.
```

---

## Cross-Cutting Python Concepts

### Type hints

**What is `Any`?**
```
A special type hint meaning "any type is acceptable." It disables type checking for that variable. Import from `typing`.
```

**`list[dict]` vs `List[Dict]`?**
```
`list[dict]` uses built-in generics (PEP 585, Python 3.9+). `List[Dict]` from `typing` is the old form, now redundant. Use `list[dict]` for 3.9+.
```

**How to read `Callable[[int, str], bool]`?**
```
A callable that takes an `int` and a `str` as arguments and returns a `bool`.
```

**Are type hints enforced at runtime?**
```
No. They are purely informational. Tools like `mypy` and `pyright` check them statically.
```

---

### Iterators and iterables

**Difference between iterable and iterator?**
```
An iterable has `__iter__` and returns an iterator. An iterator has `__iter__` and `__next__` — it maintains state and produces values one at a time.
```

**What is a generator?**
```
A function that uses `yield`. Each call to `next()` resumes execution until the next `yield`. It is an iterator that is also lazy.
```

---

### flake8

**What does flake8 check?**
```
PEP8 style (line length, spacing, indentation), logical errors (undefined names, unused imports), and code complexity.
```

**Default line length limit?**
```
79 characters.
```

**How to ignore a rule inline?**
```
`# noqa: E501` at the end of the line. Use sparingly.
```

---

## Deep Conceptual Questions

**What is referential transparency?**
```
A function call can be replaced by its return value without changing program behavior. Only possible for pure functions with no side effects.
```

**What is currying vs partial application?**
```
Currying: `f(a, b, c)` → `f(a)(b)(c)` — always one argument at a time, always returns unary functions. Partial application: fix any number of arguments at once. `functools.partial` does partial application, not currying.
```

**What is function composition formally?**
```
`compose(f, g)(x) == f(g(x))`. A general implementation:
```
```python
def compose(f, g):
    return lambda x: f(g(x))
```

**Why does Python not optimize tail recursion?**
```
Guido van Rossum deliberately chose not to — it hides stack frames and makes debugging harder. Python keeps the full call stack intentionally.
```

**The mutable default argument bug:**
```python
def make_counter(start=[]):
    start.append(1)
    return len(start)
```
The default `[]` is created once at function definition, not on each call. Every call shares the same list. Counter grows permanently. Use `start=None` and `if start is None: start = []` instead.

---

## Self-Test — Answers

**1.** `list(filter(lambda x: x > 2, [1, 2, 3, 4]))` → `[3, 4]`

**2.** `list(map(lambda x: x * 2, [1, 2, 3]))` → `[2, 4, 6]`

**3.** `functools.reduce(lambda a, b: a + b, [1, 2, 3, 4])` → `10`

**4.** `callable(42)` → `False`

**5.**
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

f = outer()
g = outer()
print(f(), f(), g())  # → 11 12 11
```
`f` and `g` are independent closures with independent `x` variables. `f()` → 11, `f()` → 12, `g()` → 11.

**6.** `functools.wraps(func)` sets `wrapper.__name__` to `func.__name__` — the original function's name.

**7.** `@staticmethod` receives no implicit first argument. `@classmethod` receives `cls` — the class itself. Static cannot access instance or class state. Classmethod can access and modify class state.

**8.** `bool` is a subclass of `int`. singledispatch walks the MRO. Finding no `bool` handler, it resolves to the `int` handler.

**9.** `functools.reduce(lambda a, b: a+b, [])` raises `TypeError: reduce() of empty iterable with no initial value`.

**10.** The 3 conditions for a closure:
1. A nested function exists.
2. The nested function references a variable from the enclosing function.
3. The enclosing function returns the nested function.

---

## Resources

- [Python docs — functools](https://docs.python.org/3/library/functools.html)
- [Python docs — collections.abc](https://docs.python.org/3/library/collections.abc.html)
- [PEP 3107 — Function Annotations](https://peps.python.org/pep-3107/)
- [PEP 585 — Built-in generics](https://peps.python.org/pep-0585/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [Real Python — Closures](https://realpython.com/inner-functions-what-are-they-good-for/)
- [Real Python — Decorators](https://realpython.com/primer-on-python-decorators/)

### AI Usage in This Project
- Documentation
- Code review
- Concept clarification
