from string import Template

t = Template("Hey, $name!")
print(t.substitute(name="John"))
