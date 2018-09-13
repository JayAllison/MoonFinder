// a knob to go onto a 5/16" bolt (AMD)
// hexagonal bolt head is 12.5 mm across the flats, 14.3 mm across the corners, 5.0 mm thick

knob_diameter = 25;
head_diameter = 14.5;
head_thickness = 5;

difference() {
    cylinder(h=2*head_thickness, d=knob_diameter, center=false, $fn=12);
    translate([0, 0, head_thickness])
        cylinder(h=head_thickness+0.1, d=head_diameter, center=false, $fn=6);
}

