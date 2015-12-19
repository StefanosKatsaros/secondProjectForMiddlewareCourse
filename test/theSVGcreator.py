import FbxCommon

file = open('cube.svg', 'w');
sdk_manager, scene = FbxCommon.InitializeSdkObjects()

if not FbxCommon.LoadScene(sdk_manager, scene, 'findMe2.fbx'):
    print('cant open file')

def draw_points(node):
    mesh = node.GetMesh();
    if mesh:
        for i in mesh.GetPolygonVertices():
            point = mesh.GetControlPointAt(i)
            file.write('%d,%d ' % (100+point[0], 200-point[1]))                # display point in explorer

    for i in range(node.GetChildCount()):
        draw_points(node.GetChild(i))


file.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="500" height="500">')
file.write('<polygon points="')
draw_points(scene.GetRootNode())
file.write('" stroke="blue" stroke-width="0.1" fill="none" transform= "skewX(25)"/>')   #"rotate(15 100 100)" "matrix(0.707 0.409 -0.707 0.409 100.51 -14.78)" "scale(2)"
file.write('</svg>')
