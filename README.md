# tex

goes through a file with name and url separated and creates .bib file to be used in tex.
```python
# ./reports/mybib.source
name www.example.com
```

```python
# ./reports/mybib.bib
@online{name,
    url = {www.example.com}
}
```

