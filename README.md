   In this document I will be explaining the process I followed to generate an SVG file that will display an FBX model, using a python XML library. Furthermore I have added additional files that I believe are very useful for any artist or programmer, when it comes to displaying 3d models. I will begin by explaining terms that were needed for the development of the project, and then proceed with the analysis of my code and my methodology to achieve the completion of the project.
    
   To begin with, FBX is a proprietary file format which is owned by Autodesk and is created by exporting models in .fbx format. It is one of the most commonly used file formats in gaming, since they have are of smaller file size, they keep information that assist game engines and are very easy to use. Modelling artists also use .fbx files as a method of displaying their work publicly on web pages, but also sell their models which can also contain animations. Secondly, SVG stands for Scalable Vector Graphics and is used to define vector-based graphics for the Web. It defines the graphics in XML format and the graphics don’t lose any quality if they are zoomed or resized. The greatest benefits of using SVG is that images can be created and edited with a text editor, they can be searched, indexed, scripted and compressed, they are scalable and can be printed with high quality at any resolution and finally they are zoomable. Therefore since we have got around these 2 basic concepts I will be explaining how I used python to generate an SVG file that will display an FBX file.
    
   We begin by creating an object in 3Ds max and exporting in to our folder in an .fbx format. Then we create in the same file a .py document, and the python coding begins. At the top of our .py file we import the FbxCommon library to be able to use the attributes we want. Then we find the findMe2.fbx (my .fbx file) and we begin by reading the vertices and indices to begin forming the shape of the fbx. Furthermore we proceed by telling where the points will be displayed. Finally using xml techniques which we embed in python we are able to set the width and the height of our fbx display area, the actual points that will be drawn, the color of the shape and the filling and finally its rotation, scale and whatever else we want. Rotations can be used in several ways, such as skewing, rotating and using a matrix, and I have commented out the ones I did not use. Finally we stop the reading-file process. This process will create an .svg file which we can open up with a web browser and display the .fbx file. The .fbx file that I used contains a 3D teapot model and it is displayed like this in the web browser: 
  
(please see Word Document for images)

   This simple method is an excellent way for artists to display their models such as this publicly on a website or such. Wanting to add to the python-svg-fbx combination, I wanted to give a different approach for displaying 3D models online. Besides using .fbx there is another export option which seems to be very useful, especially to artists with basic programming skills. Exporting a model to a .x3d format allows an automated process to take place and for us to be given with an .html file which is easy to integrate in our webpage. Once exported we can use x3dom.com and convert the information copied from the xml format of the .x3d file to .html format. Later we can use this information and implement it into our .html. I have provided an example, using a .x3d file exported from blender, I made the transition and have a index.html file which can be opened up and the monkey with a hat can be viewed. This is an extremely useful process because we can have an entire scene including all complex models, cameras and lightings available for view with great ease. Of course there are benefits and downsides.
    
(please see Word Document for images)

   Furthermore, to give a different approach for both game programmers and artists, unity is a great tool for working in web browsers (all but chrome that is). In the folder unityWebGL I have created an .html page which used the a .unity3d file to display a small game I created. This includes models and programming files which unity compresses and creates for us when building for webGL. Although this is quite far from the SVG assignment, I thought it was worth creating since it is worth using all available tools out there (with caution). Again like the .x3d the final version is an .html document which we can process and use into our webpage in a very simple and clear manner.
 
 (please see Word Document for images)

