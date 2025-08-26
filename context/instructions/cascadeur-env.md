# Information about cascadeur built-in python environment

Cascadeur has a built-in python environment, which:
- DOES NOT print to console, to see any output, you need to write to a file
- Sockets are blocked, you cannot use socket api, or any library that uses socket api
- Only for interactive use, much like jupyter notebook (but no print), the states are preserved once you run a block of code, never cleans up unless you restart cascadeur. So, DO NOT wrap your code in a function, and DO NOT use `if __name__ == "__main__":` block, because that would make your code not work in cascadeur interactive python environment.

## References
- [Cascadeur Python Local Documentation](casey-docs\markdown)
- [Cascadeur Python Remote Documentation](https://cascadeur.com/python-api/)
