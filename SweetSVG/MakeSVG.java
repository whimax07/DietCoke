import shapes.Polygon;

import java.io.File;

public class MakeSVG {

    public static void main(String[] args) {
        BaseSVG baseSVG = new BaseSVG();

        Polygon triangle = new Polygon()
                .addPoint(20, 20)
                .addPoint(130, 40)
                .addPoint(70, 140);

        triangle
                .addStyleAttribute("fill", "blue")
                .addStyleAttribute("stroke", "DarkBlue")
                .addStyleAttribute("stroke-width", "2");

        baseSVG.addElement(triangle);

        baseSVG.writeImage(new File("TestTriangle.svg"));

    }

}
