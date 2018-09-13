// a foot to go onto a 5/16" bolt (AMD)
// bolt shaft is 7.5-8 mm across

shaft_diameter = 8;
shaft_depth = 5;
foot_diameter = 1.5*shaft_diameter;

difference() {
    cylinder(h=2*shaft_depth, d=foot_diameter, center=false, $fn=16);
    translate([0, 0, shaft_depth])
        cylinder(h=shaft_depth+0.1, d=shaft_diameter, center=false, $fn=16);
}

