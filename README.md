# sections-subsections-app
A simple app to create and show the hierarchical data
# Internal Logic
I've used the django-mptt library to generate and show the hierarchical data.
The approach is very simple and straight forward.
If a section has no parent then it's a new section.
And if a section has a parent then it's a sub section of the selected section.

To Create a Prent or Main Section Just leave the dropdown Empty and to create a Child or Sub section just select the Parent Section from the Drop Down List.

# Backend Logic

In case of Child or subsection, the parent will be selected and Searched by the name.

