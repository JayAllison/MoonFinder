// edit these values to configure the bracket
telescope_OD = 116;
bracket_thickness = 4;
bracket_width = 12;
screw_diameter = 3.5;

// these values are calculated - do not edit
inner_diameter = telescope_OD;
outer_diameter = telescope_OD + 2*bracket_thickness;

screwplate_length = bracket_thickness + 3*screw_diameter;

union() {
    // build the 180-degree arc of the bracket to the specified diameter and thickness
    difference() {
        cylinder(h=bracket_width, d=outer_diameter, center=true, $fn=256);
        cylinder(h=bracket_width*2, d=inner_diameter, center=true, $fn=256);
        translate([0, -outer_diameter/2, -bracket_width]) 
            cube(size=[outer_diameter, outer_diameter, bracket_width*2], center=false);
    }
    // add a screwplate to one end
    difference() {
        translate([-bracket_thickness/2, -(inner_diameter+screwplate_length)/2, 0]) 
            cube(size=[bracket_thickness, screwplate_length, bracket_width], center=true);
        translate([-bracket_thickness/2, -(inner_diameter+screwplate_length)/2, 0]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
    }
    // add a screwplate to the other end
    difference() {
        translate([-bracket_thickness/2, (inner_diameter+screwplate_length)/2, 0]) 
            cube(size=[bracket_thickness, screwplate_length, bracket_width], center=true);
        translate([bracket_thickness/2, (inner_diameter+screwplate_length)/2, 0]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
    }
}