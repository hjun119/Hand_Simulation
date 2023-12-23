/*
최초작성자 : 정해준
최초작성일 : 2023.12.22.
최종변경일 : 2023.12.22.
목적 : c++ 테스트
개정이력 : 정해준, 2023.12.22, 프로그램 제작
저작권 : 정해준
*/
#include <vtkActor.h>
#include <vtkNamedColors.h>
#include <vtkNew.h>
#include <vtkPolyDataMapper.h>
#include <vtkProperty.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkRenderer.h>
#include <vtkSTLReader.h>

/*
목적 : STL파일 출력
객체 :   colors : 
        reader : STL파일을 읽어오는 역할 
        mapper : STL에서 읽어온 polydata(mesh)를 그래픽 장면에 나타낼 수 있는 형태로 변환해주는 역할
        actor  : STL파일을 mapper를 통해 변환시킨 객체를 표현해주는 역할
        renderer : 3D 장면을 구성하고 구현하는 역할(랜더링)
                    actor들을 관리하며 적절한 순서로 그려서 화면에 3D 장면을 표시해줌
        renderWindow : 3D장면을 표시해주는 창을 관리하는 역할
        renderWindowInteractor : 3D장면과 사용자의 상호작용을 도와주는 역할
                                    ex) 마우스 이벤트 처리, 확대/축소, 사용자 입력 처리 등
반환값 : -
개정이력 : 정해준, 2023.12.23, 제작중...
*/
int main(int argc, char* argv[]) {
    vtkNew<vtkNamedColors> colors;

    if (argc != 2){
        cout << "Required parameters : Filename(.stl) e.g ./stl/tester.stl" << endl;
        return EXIT_FAILURE;
    }

    std::string inputFilename = argv[1];

    vtkNew<vtkSTLReader> reader;
    reader->SetFileName(inputFilename.c_str());
    reader->Update();

    vtkNew<vtkPolyDataMapper> mapper;
    mapper->SetInputConnection(reader->GetOutputPort());

    vtkNew<vtkActor> actor;
    actor->SetMapper(mapper);
    actor->GetProperty()->SetDiffuse(0.8);
    actor->GetProperty()->SetDiffuseColor(
        colors->GetColor3d("LightSteelBlue").GetData());
    actor->GetProperty()->SetSpecular(0.3);
    actor->GetProperty()->SetSpecularPower(60.0);

    vtkNew<vtkRenderer> renderer;
    vtkNew<vtkRenderWindow> renderWindow;
    renderWindow->AddRenderer(renderer);
    renderWindow->SetWindowName("ReadSTL");

    vtkNew<vtkRenderWindowInteractor> renderWindowInteractor;
    renderWindowInteractor->SetRenderWindow(renderWindow);

    renderer->AddActor(actor);
    renderer->SetBackground(colors->GetColor3d("DarkOliveGreen").GetData());

    renderWindow->Render();
    renderWindowInteractor->Start();

    return EXIT_SUCCESS;
}
