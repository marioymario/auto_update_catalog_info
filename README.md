# auto_update_catalog_info

This repo is  a system for ingredients. It update a catalog with information related to the data provided by suppliers.
The suppliers send a picture (.tif) and text with descriptions and basic information (.txt)
The text needs is turned into an HTML file that shows the image and the product description. 
The contents of the HTML file is uploaded to a web service that is running with Django.

Parts:

 - A script that summarizes and processes sales data into different categories.
 - A script Generate a PDF using Python.
 - A script Automatically send a PDF by email.
 - A script Write a script to check the health status of the system.

