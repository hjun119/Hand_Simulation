
import sys

import vtk
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

###########################################################################################################
#                                             file name
filenames_palm = ["./stl/6/p_1.stl"]
filenames_finger1 = ["./stl/1/f_1.stl","./stl/1/f_2.stl","./stl/1/f_3.stl"]
filenames_finger2 = ["./stl/2/f_1.stl","./stl/2/f_2.stl","./stl/2/f_3.stl","./stl/2/f_4.stl"]
filenames_finger3 = ["./stl/3/f_1.stl","./stl/3/f_2.stl","./stl/3/f_3.stl","./stl/3/f_4.stl"]
filenames_finger4 = ["./stl/4/f_1.stl","./stl/4/f_2.stl","./stl/4/f_3.stl","./stl/4/f_4.stl"]
filenames_finger5 = ["./stl/5/f_1.stl","./stl/5/f_2.stl","./stl/5/f_3.stl","./stl/5/f_4.stl"]

###########################################################################################################
#                                             file offset
offsets_x_palm, offsets_y_palm, offsets_z_palm = [0, 0, 0]
offsets_x_finger1 = [0, 0, 0]
offsets_y_finger1 = [0, 0, 0]
offsets_z_finger1 = [0, 0, 0]
offsets_x_finger2 = [0, 0, 0, 0]
offsets_y_finger2 = [0, 0, 0, 0]
offsets_z_finger2 = [0, 0, 0, 0]
offsets_x_finger3 = [0, 0, 0, 0]
offsets_y_finger3 = [0, 0, 0, 0]
offsets_z_finger3 = [0, 0, 0, 0]
offsets_x_finger4 = [0, 0, 0, 0]
offsets_y_finger4 = [0, 0, 0, 0]
offsets_z_finger4 = [0, 0, 0, 0]
offsets_x_finger5 = [0, 0, 0, 0]
offsets_y_finger5 = [0, 0, 0, 0]
offsets_z_finger5 = [0, 0, 0, 0]

###########################################################################################################
#                                             origin
finger2_1 = [-152.5,0,14.75]
finger2_2 = [-95,0,2]
finger2_3 = [5,0,-2]
finger2_4 = [65,0,2]
finger3_1 = [-138,0,-35.5]
finger3_2 = [-79,0,2]
finger3_3 = [20,0,-2]
finger3_4 = [79.5,0,2]
finger4_1 = [-152,0,-86]
finger4_2 = [-94,0,2]
finger4_3 = [5,0,-2]
finger4_4 = [64,0,2]
finger5_1 = [-182,0,-135]
finger5_2 = [-124,0,2]
finger5_3 = [-65,0,-2]
finger5_4 = [-6,0,2]

scale = 1.0
dt = 1.0

actor_palm = list()
actor_finger1 = list()
actor_finger2 = list()
actor_finger3 = list()
actor_finger4 = list()
actor_finger5 = list()
assemble_hand = list()
assemble_finger1 = list()
assemble_finger2 = list()
assemble_finger3 = list()
assemble_finger4 = list()
assemble_finger5 = list()

zoom_factor = 1.0

class Simulation(QWidget):
    def __init__(self):
        super().__init__()

        self.robot_sim_ren = vtk.vtkRenderer()
        self.render_window = vtk.vtkRenderWindow()
        self.render_window.SetSize(1200,1000)

        self.style =  vtk.vtkInteractorStyle()
        self.robot_sim = QVTKRenderWindowInteractor(self)

        self.robot_sim_ren.SetBackground(1, 1, 1)
        self.robot_sim.GetRenderWindow().AddRenderer(self.robot_sim_ren)
        self.robot_sim.SetSize(1200,1000)

        self.robot_sim.SetInteractorStyle(self.style)
        self.robot_sim.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())

        self.robot_sim_cam_config()
        self.MakeActor_palm()
        self.MakeActor_finger1()
        self.MakeActor_finger2()
        self.MakeActor_finger3()
        self.MakeActor_finger4()
        self.MakeActor_finger5()
        self.MakeAssemble_finger1()
        self.MakeAssemble_finger2()
        self.MakeAssemble_finger3()
        self.MakeAssemble_finger4()
        self.MakeAssemble_finger5()
        self.MakeAssemble_hand()
        self.SetOriginAssemble()
        self.robot_sim_draw()
        self.set_robot_sim_joint_locations()
        
        self.show_sim()
        #iren = vtk.vtkRenderWindowInteractor()
        #iren.SetRenderWindow(self.render_window)
        #self.robot_sim.Initialize()
        #self.render_window.Render()
        #self.robot_sim.Start()

        #self.show()

    def sim_out(self):
        rbsim=self.robot_sim
        print(rbsim)

        return rbsim
    
    def show_sim(self):
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(self.render_window)
        self.robot_sim.Initialize()
        self.robot_sim.Start()

        self.show()

    # def robot_sim_widget(self):
    #     robot_sim_widget = self.robot_sim
    #     return robot_sim_widget
    
    # def robot_sim_start(self):
        


    def set_robot_sim_joint_locations(self):
        #self.j_data_0,self.j_data_1,self.j_data_2,self.j_data_3,self.j_data_4,self.j_data_5 = map(float,self.Joint_data)
        assemble_finger2[0].SetOrientation(0,-10,0)
        assemble_finger2[1].SetOrientation(0,0,-90)
        assemble_finger2[2].SetOrientation(0,0,-90)
        assemble_finger2[3].SetOrientation(0,0,-90)
        assemble_finger3[0].SetOrientation(0,-10,0)
        assemble_finger3[1].SetOrientation(0,0,-90)
        assemble_finger3[2].SetOrientation(0,0,-90)
        assemble_finger3[3].SetOrientation(0,0,-90)
        assemble_finger4[0].SetOrientation(0,0,0)
        assemble_finger4[1].SetOrientation(0,0,-90)
        assemble_finger4[2].SetOrientation(0,0,-90)
        assemble_finger4[3].SetOrientation(0,0,-90)
        assemble_finger5[0].SetOrientation(0,0,0)
        assemble_finger5[1].SetOrientation(0,0,-90)
        assemble_finger5[2].SetOrientation(0,0,-90)
        assemble_finger5[3].SetOrientation(0,0,-90)

        # assemble[1].SetOrientation(0,0,self.j_data_0)
        # assemble[2].SetOrientation(-self.j_data_1,0,0)
        # assemble[3].SetOrientation(-self.j_data_2,0,0)
        # assemble[4].SetOrientation(-self.j_data_3,0,0)
        # assemble[5].SetOrientation(0,0,self.j_data_4)
        # assemble[6].SetOrientation(-self.j_data_5,0,0)

    def robot_sim_cam_config(self):
        self.camera = self.robot_sim_ren.GetActiveCamera()

        self.camera.SetFocalPoint(0, 0, 0)
        self.camera.SetPosition(0, -650, 300)

        self.robot_sim_ren.SetActiveCamera(self.camera)

    def LoadSTL(self, filename):
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        mapper = vtk.vtkPolyDataMapper() # maps polygonal data to graphics primitives
        mapper.SetInputConnection(reader.GetOutputPort())
        actor = vtk.vtkLODActor()
        actor.SetMapper(mapper)
        # self.robot_sim_ren.AddActor(actor)

        return actor # represents an entity in a rendered scene
    


###########################################################################################################
#                                             make actor
    def MakeActor_palm(self):
        for id, file in enumerate(filenames_palm):
            actor_palm.append(self.LoadSTL(file))
            actor_palm[id].SetScale(scale)
            actor_palm[id].SetPosition(offsets_x_finger1[id], offsets_y_finger1[id], offsets_z_finger1[id])
            actor_palm[id].GetProperty().SetColor(1,1,1)
            actor_palm[id].GetProperty().SetMetallic(1)
            actor_palm[id].GetProperty().SetDiffuse(1)
            actor_palm[id].GetProperty().SetSpecular(0.1)

    def MakeActor_finger1(self):
        for id, file in enumerate(filenames_finger1):
            actor_finger1.append(self.LoadSTL(file))
            actor_finger1[id].SetScale(scale)
            actor_finger1[id].SetPosition(offsets_x_finger1[id], offsets_y_finger1[id], offsets_z_finger1[id])
            actor_finger1[id].GetProperty().SetColor(1,1,1)
            actor_finger1[id].GetProperty().SetMetallic(1)
            actor_finger1[id].GetProperty().SetDiffuse(1)
            actor_finger1[id].GetProperty().SetSpecular(0.1)
            # actor[id].GetProperty().SetSpecularColor(.01,.01,.01)
    
    def MakeActor_finger2(self):
        for id, file in enumerate(filenames_finger2):
            actor_finger2.append(self.LoadSTL(file))
            actor_finger2[id].SetScale(scale)
            actor_finger2[id].SetPosition(offsets_x_finger2[id], offsets_y_finger2[id], offsets_z_finger2[id])
            actor_finger2[id].GetProperty().SetColor(1,1,1)
            actor_finger2[id].GetProperty().SetMetallic(1)
            actor_finger2[id].GetProperty().SetDiffuse(1)
            actor_finger2[id].GetProperty().SetSpecular(0.1)

    def MakeActor_finger3(self):
        for id, file in enumerate(filenames_finger3):
            actor_finger3.append(self.LoadSTL(file))
            actor_finger3[id].SetScale(scale)
            actor_finger3[id].SetPosition(offsets_x_finger3[id], offsets_y_finger3[id], offsets_z_finger3[id])
            actor_finger3[id].GetProperty().SetColor(1,1,1)
            actor_finger3[id].GetProperty().SetMetallic(1)
            actor_finger3[id].GetProperty().SetDiffuse(1)
            actor_finger3[id].GetProperty().SetSpecular(0.1)

    def MakeActor_finger4(self):
        for id, file in enumerate(filenames_finger4):
            actor_finger4.append(self.LoadSTL(file))
            actor_finger4[id].SetScale(scale)
            actor_finger4[id].SetPosition(offsets_x_finger4[id], offsets_y_finger4[id], offsets_z_finger4[id])
            actor_finger4[id].GetProperty().SetColor(1,1,1)
            actor_finger4[id].GetProperty().SetMetallic(1)
            actor_finger4[id].GetProperty().SetDiffuse(1)
            actor_finger4[id].GetProperty().SetSpecular(0.1)
    
    def MakeActor_finger5(self):
        for id, file in enumerate(filenames_finger5):
            actor_finger5.append(self.LoadSTL(file))
            actor_finger5[id].SetScale(scale)
            actor_finger5[id].SetPosition(offsets_x_finger5[id], offsets_y_finger5[id], offsets_z_finger5[id])
            actor_finger5[id].GetProperty().SetColor(1,1,1)
            actor_finger5[id].GetProperty().SetMetallic(1)
            actor_finger5[id].GetProperty().SetDiffuse(1)
            actor_finger5[id].GetProperty().SetSpecular(0.1)
            


###########################################################################################################
#                                             make assemble
    def MakeAssemble_hand(self):
        assemble_hand.append(vtk.vtkAssembly())
        assemble_hand[0].AddPart(actor_palm[0])
        assemble_hand[0].AddPart(assemble_finger1[0])
        assemble_hand[0].AddPart(assemble_finger2[0])
        assemble_hand[0].AddPart(assemble_finger3[0])
        assemble_hand[0].AddPart(assemble_finger4[0])
        assemble_hand[0].AddPart(assemble_finger5[0])

    def MakeAssemble_finger1(self):
        for id, value in enumerate(actor_finger1):
            assemble_finger1.append(vtk.vtkAssembly())
            assemble_finger1[id].AddPart(actor_finger1[id])
        for id, value in enumerate(assemble_finger1[0:-1]):
            assemble_finger1[id].AddPart(assemble_finger1[id+1])

    def MakeAssemble_finger2(self):
        for id, value in enumerate(actor_finger2):
            assemble_finger2.append(vtk.vtkAssembly())
            # assemble_finger2[id].AddPart(actor_finger2[id])
        # for id, value in enumerate(assemble_finger2[:-1]):
        #     assemble_finger2[id].AddPart(assemble_finger2[id+1])
        assemble_finger2[0].AddPart(assemble_finger2[1])
        assemble_finger2[0].AddPart(actor_finger2[3])
        assemble_finger2[1].AddPart(assemble_finger2[2])
        assemble_finger2[1].AddPart(actor_finger2[2])
        assemble_finger2[2].AddPart(assemble_finger2[3])
        assemble_finger2[2].AddPart(actor_finger2[1])
        assemble_finger2[3].AddPart(actor_finger2[0])
        
        

    def MakeAssemble_finger3(self):
        for id, value in enumerate(actor_finger3):
            assemble_finger3.append(vtk.vtkAssembly())
        assemble_finger3[0].AddPart(assemble_finger3[1])
        assemble_finger3[0].AddPart(actor_finger3[3])
        assemble_finger3[1].AddPart(assemble_finger3[2])
        assemble_finger3[1].AddPart(actor_finger3[2])
        assemble_finger3[2].AddPart(assemble_finger3[3])
        assemble_finger3[2].AddPart(actor_finger3[1])
        assemble_finger3[3].AddPart(actor_finger3[0])

    def MakeAssemble_finger4(self):
        for id, value in enumerate(actor_finger4):
            assemble_finger4.append(vtk.vtkAssembly())
        assemble_finger4[0].AddPart(assemble_finger4[1])
        assemble_finger4[0].AddPart(actor_finger4[3])
        assemble_finger4[1].AddPart(assemble_finger4[2])
        assemble_finger4[1].AddPart(actor_finger4[2])
        assemble_finger4[2].AddPart(assemble_finger4[3])
        assemble_finger4[2].AddPart(actor_finger4[1])
        assemble_finger4[3].AddPart(actor_finger4[0])

    def MakeAssemble_finger5(self):
        for id, value in enumerate(actor_finger5):
            assemble_finger5.append(vtk.vtkAssembly())
        assemble_finger5[0].AddPart(assemble_finger5[1])
        assemble_finger5[0].AddPart(actor_finger5[3])
        assemble_finger5[1].AddPart(assemble_finger5[2])
        assemble_finger5[1].AddPart(actor_finger5[2])
        assemble_finger5[2].AddPart(assemble_finger5[3])
        assemble_finger5[2].AddPart(actor_finger5[1])
        assemble_finger5[3].AddPart(actor_finger5[0])
        
        # assemble[1].SetOrientation(0,0,0)
        # assemble[2].SetOrientation(9,0,0)
        # assemble[3].SetOrientation(113,0,0)
        # assemble[4].SetOrientation(0,0,76)
        # assemble[5].SetOrientation(109,0,0)
        # assemble[6].SetOrientation(0,0,-210)


###########################################################################################################
#                                             setorigin(원점설정)
    def SetOriginAssemble(self):
        assemble_finger2[0].SetOrigin(finger2_1)
        assemble_finger2[1].SetOrigin(finger2_2)
        assemble_finger2[2].SetOrigin(finger2_3)
        assemble_finger2[3].SetOrigin(finger2_4)
        assemble_finger3[0].SetOrigin(finger3_1)
        assemble_finger3[1].SetOrigin(finger3_2)
        assemble_finger3[2].SetOrigin(finger3_3)
        assemble_finger3[3].SetOrigin(finger3_4)
        assemble_finger4[0].SetOrigin(finger4_1)
        assemble_finger4[1].SetOrigin(finger4_2)
        assemble_finger4[2].SetOrigin(finger4_3)
        assemble_finger4[3].SetOrigin(finger4_4)
        assemble_finger5[0].SetOrigin(finger5_1)
        assemble_finger5[1].SetOrigin(finger5_2)
        assemble_finger5[2].SetOrigin(finger5_3)
        assemble_finger5[3].SetOrigin(finger5_4)
        

    def robot_sim_draw(self):
        # Reset the camera to view the dataset
        self.robot_sim_ren.ResetCamera()

        # Zoom factor
        self.robot_sim_ren.GetActiveCamera().Zoom(zoom_factor)

        # Add the actor to the vtkRenderer
        self.robot_sim_ren.AddActor(assemble_hand[0])
        self.robot_sim_ren.AddActor(assemble_finger1[0])
        self.robot_sim_ren.AddActor(assemble_finger2[0])
        self.robot_sim_ren.AddActor(assemble_finger3[0])
        self.robot_sim_ren.AddActor(assemble_finger4[0])
        self.robot_sim_ren.AddActor(assemble_finger5[0])
        
        # Set the background color to the vtkRenderer
        self.robot_sim_ren.SetBackground(.2,.2,.2)

        # Render the scene
        self.robot_sim.Render()
        




if __name__ == "__main__":
    # Set up the PySide6 application
    app = QApplication(sys.argv)
    widget = Simulation()
    widget.resize(800,600)
    #widget.show()

    # Start the PySide6 application event loop
    sys.exit(app.exec())
