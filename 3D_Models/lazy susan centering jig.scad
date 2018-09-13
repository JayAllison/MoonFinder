// create a jig that fits in the center of the lazy susan bearing and aligns the bearing with the pin hole

hole_diameter = 33;
hole_height = 8;

pin_diameter = 3;
pin_height = 5;

union() {
    cylinder(h=hole_height, d=hole_diameter, center=false, $fn=256);
    translate([0,0,hole_height])
        cylinder(h=pin_height, d=pin_diameter, center=false, $fn=256);
}