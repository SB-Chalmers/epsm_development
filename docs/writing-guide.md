# Writing for people

Write as if you are explaining the work to a new colleague. Help them understand what the code does, how to use it and what to check. They should not need to know the whole EPSM platform before trying one example.

## Give a useful instruction

Name the action, the object and the result. Use ordinary words and short paragraphs. Put steps in the order someone will follow them.

| Instead of | Write |
| --- | --- |
| Ensure interoperability across package boundaries | Check that the next package can read this package's output. |
| Leverage the canonical artifacts | Use the saved inputs and results. |
| Establish a coherent validation pipeline | Run the input checks, then run the simulation tests. |
| Promote the candidate after passing the gates | After the checks pass, make the new database release the default. |
| Provide developer-facing abstractions | Give developers clear classes and functions. |

These are examples, not banned words. Use a technical term when it helps explain the work. Define it when a new contributor might not know it. Keep exact code names, units, versions and scientific meanings accurate.

## Explain code with enough detail

A good docstring answers practical questions:

- What does this function or object do?
- What inputs does it need, and what are their units?
- What does it return?
- Does it change an object, read a file, write output or contact a service?
- What can go wrong, and what should the caller do?
- What does a small working example look like?

Keep the detailed documentation used in EPSM Core. Make each explanation specific to the code. Remove repeated paragraphs that add no information. A simple helper needs less explanation than a calculation with physical assumptions.

When a choice matters, explain why it was made. For example: “The writer refuses to replace an existing file unless the caller asks for replacement. This keeps earlier study inputs safe.”

## Make examples easy to follow

Start with one small task and known inputs. Show the public call, inspect the result and check a useful value. Explain the setup before the code. Let the next example build on the idea, without depending on variables left over from the first notebook.

Use [docstring examples](docstrings-and-api-docs.md) for a short public call. Use a notebook for teaching a longer task and a test for checking behaviour. Link them when they describe the same task. Mark an API idea clearly when it has not been implemented.

## Describe what was checked

State the actual check and result. “Both notebooks ran from fresh kernels” is more useful than “the examples are robust.” Explain a failure or missing check plainly.

Keep software checks separate from scientific accuracy. A completed simulation shows that the selected inputs ran; comparison with measured buildings needs its own evidence.

Use accurate project information. Record the real contributors, license, sources and dates. Do not add names or claims just to fill a template.

## Read before committing

Read the text once as someone new to the task. Ask:

1. Can I tell what to do first?
2. Are unfamiliar terms explained?
3. Does every sentence add something useful?
4. Do the examples match the code and its current status?
5. Can I tell what was checked and what is still unknown?

Read an awkward sentence aloud and rewrite it in the words you would use with a colleague. Keep the instructions clear, respectful and direct.
