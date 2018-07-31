// edit these values to configure the bracket
// 116 was too small, 120 was slightly too big, so next we'll try 119
telescope_OD = 119;
bracket_thickness = 4;
bracket_width = 30;

axle_diameter = 6;
knob_thickness = 15;

screw_diameter = 3.5;

// these values are calculated - do not edit
inner_diameter = telescope_OD;
outer_diameter = telescope_OD + 2*bracket_thickness;
bracket_center_radius = (inner_diameter + outer_diameter) / 4;
screwplate_length = bracket_thickness + 3*screw_diameter;

// using a six-sided circle as a hexagon means the hexagon will be slightly smaller than the circle
// circle diameter * cos(30) = hexagon width, flat side to flat side
knob_diameter = bracket_width / cos(30);

// put it all together
union() {
    // subtract the axle hole from the bracket
    difference() {
        // put the knob onto the bracket
        union() {
            // build the 180-degree arc of the bracket to the specified diameter and thickness
            difference() {
                cylinder(h=bracket_width, d=outer_diameter, center=true, $fn=256);
                cylinder(h=bracket_width*2, d=inner_diameter, center=true, $fn=256);
                translate([0, -outer_diameter/2, -bracket_width]) 
                    cube(size=[outer_diameter, outer_diameter, bracket_width*2], center=false);
            }
            // add the pivot point (knob)
            translate([-bracket_center_radius - knob_thickness/2, 0, 0])
                rotate([90, 0, 90])
                    cylinder(h=knob_thickness, d=knob_diameter, $fn=6, center=true);
        }
        // add the axle hole through the knob and the bracket
        translate([-bracket_center_radius - knob_thickness/2, 0, 0])
            rotate([90, 0, 90])
                    cylinder(h=knob_thickness*2, d=axle_diameter, $fn=256, center=true);
    }
    // add a screwplate to one end
    difference() {
        translate([-bracket_thickness/2, -(inner_diameter+screwplate_length)/2, 0]) 
            cube(size=[bracket_thickness, screwplate_length, bracket_width], center=true);
        translate([-bracket_thickness/2, -(inner_diameter+screwplate_length)/2, bracket_width/3]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
        translate([-bracket_thickness/2, -(inner_diameter+screwplate_length)/2, -bracket_width/3]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
    }
    // add a screwplate to the other end
    difference() {
        translate([-bracket_thickness/2, (inner_diameter+screwplate_length)/2, 0]) 
            cube(size=[bracket_thickness, screwplate_length, bracket_width], center=true);
        translate([-bracket_thickness/2, (inner_diameter+screwplate_length)/2, bracket_width/3]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
        translate([-bracket_thickness/2, (inner_diameter+screwplate_length)/2, -bracket_width/3]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
    }
}