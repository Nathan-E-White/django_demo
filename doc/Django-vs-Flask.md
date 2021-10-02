Requirement 1: Django vs. Flask


- "Pirates use Flask, the navy uses Django."

Option 1.A: Django:
i.		Full-stack web framework
ii.		Well supported, mature technology (created 2005)
iii.	Implemented in Python
iv.		Easier to use out of the box
v.		Ready to use admin framework
vi.		Built in template engine
viii.	Divide larger project into multiple small applications
ix.		Built in ORM performs common tasks without complex DB queries
x.		Production-ready framework
xi.		Less flexible framework
xii.	Suitable for large, complex projects
xiii.	Framework forces a lot of 'best practices.'
xiv.	Over 2x LOC vs Flask

Option 1.B: Flask:
i.		Light-weight extensible framework
ii.		Well supported, mature technology (created 2010)
iii.	Implemented in Python
iv.		Easier to customize for different use cases
v.		No admin framework included
vi.		Template engine is Jinja2, based on Django's template engine
viii.	Easier to add multiple views and models to a single application
ix.		ORM in Python, SQLAlchemy as toolkit. SQL queries for common tasks
x.		Single-threaded, doesn't scale well under heavy loads
xi.		Easy to use plugins and libraries as needed
xii.	Suitable for simpler projects, faster to get up and running
xiii.	Developers free to make bad choices.
xiv.	Fewer LOC for a simple page.