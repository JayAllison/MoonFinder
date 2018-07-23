telescope_OD = 116;
bracket_thickness = 4;
bracket_width = 6;

inner_diameter = telescope_OD;
outer_diameter = telescope_OD + bracket_thickness;

difference() {
    cylinder(h=bracket_width, d=outer_diameter, center=true, $fn=256);
    cylinder(h=bracket_width*2, d=inner_diameter, center=true, $fn=256);
}