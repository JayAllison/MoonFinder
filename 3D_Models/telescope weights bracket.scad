// edit these values to configure the bracket
// 116 was too small, 120 was slightly too big, so next we'll try 119
telescope_OD = 119;
bracket_thickness = 4;
bracket_width = 25;
endcap_adder = 4;
center_adjust = 5;
washer_opening = 21;
washer_stack_height = 16;
washer_separation_angle = 43;
screw_diameter = 3;

// these values are calculated - do not edit
inner_diameter = telescope_OD;
outer_diameter = telescope_OD + 2*bracket_thickness + 2*endcap_adder;
middle_diameter = telescope_OD + 2*endcap_adder;

washer_post_length = washer_stack_height + bracket_thickness;
washer_post_angled_x1 = cos(0.5*washer_separation_angle) * (outer_diameter+washer_post_length-bracket_thickness)/2;
washer_post_angled_y1 = sin(0.5*washer_separation_angle) * (outer_diameter+washer_post_length-bracket_thickness)/2;
washer_post_angled_x2 = cos(1.5*washer_separation_angle) * (outer_diameter+washer_post_length-bracket_thickness)/2;
washer_post_angled_y2 = sin(1.5*washer_separation_angle) * (outer_diameter+washer_post_length-bracket_thickness)/2;

bracket_center_radius = (inner_diameter + outer_diameter) / 4;
screwplate_length = bracket_thickness + 3*screw_diameter;

// put it all together
union() {
    // build the 180-degree arc of the bracket to the specified diameter and thickness
    difference() {
        cylinder(h=bracket_width-center_adjust, d=outer_diameter, center=true, $fn=256);
        cylinder(h=bracket_width*2, d=inner_diameter, center=true, $fn=256);
        translate([0, -outer_diameter/2, -bracket_width]) 
            cube(size=[outer_diameter, outer_diameter, bracket_width*2], center=false);
    }
    // add a screwplate to one end
    difference() {
        translate([-bracket_thickness/2, -(inner_diameter+screwplate_length+endcap_adder)/2, 0]) 
            cube(size=[bracket_thickness, screwplate_length+endcap_adder, bracket_width-center_adjust], center=true);
        *translate([-bracket_thickness/2, -(inner_diameter+screwplate_length)/2-endcap_adder, bracket_width/3 - center_adjust/2]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
        translate([-bracket_thickness/2, -(inner_diameter+screwplate_length)/2-endcap_adder, -bracket_width/3 + center_adjust/2]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
    }
    // add a screwplate to the other end
    difference() {
        translate([-bracket_thickness/2, (inner_diameter+screwplate_length+endcap_adder)/2, 0]) 
            cube(size=[bracket_thickness, screwplate_length+endcap_adder, bracket_width-center_adjust], center=true);
        *translate([-bracket_thickness/2, (inner_diameter+screwplate_length)/2+endcap_adder, bracket_width/3 - center_adjust/2]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
        translate([-bracket_thickness/2, (inner_diameter+screwplate_length)/2+endcap_adder, -bracket_width/3 + center_adjust/2]) 
            rotate([0, 90, 0]) 
                cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
    }
    // build the 180-degree arc of the bracket to the specified diameter and thickness
    translate([0, 0, bracket_width]) 
        union() {
            difference() {
                cylinder(h=bracket_width+center_adjust, d=outer_diameter, center=true, $fn=256);
                cylinder(h=bracket_width*2, d=middle_diameter, center=true, $fn=256);
                translate([0, -outer_diameter/2, -bracket_width]) 
                    cube(size=[outer_diameter, outer_diameter, bracket_width*2], center=false);
            }
            // add a screwplate to one end
            difference() {
                translate([-bracket_thickness/2, -(middle_diameter+screwplate_length)/2, 0]) 
                    cube(size=[bracket_thickness, screwplate_length, bracket_width+center_adjust], center=true);
                translate([-bracket_thickness/2, -(middle_diameter+screwplate_length)/2, bracket_width/3 + center_adjust/2]) 
                    rotate([0, 90, 0]) 
                        cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
                *translate([-bracket_thickness/2, -(middle_diameter+screwplate_length)/2, -bracket_width/3 - center_adjust/2]) 
                    rotate([0, 90, 0]) 
                        cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
            }
            // add a screwplate to the other end
            difference() {
                translate([-bracket_thickness/2, (middle_diameter+screwplate_length)/2, 0]) 
                    cube(size=[bracket_thickness, screwplate_length, bracket_width+center_adjust], center=true);
                translate([-bracket_thickness/2, (middle_diameter+screwplate_length)/2, bracket_width/3 + center_adjust/2]) 
                    rotate([0, 90, 0]) 
                        cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
                *translate([-bracket_thickness/2, (middle_diameter+screwplate_length)/2, -bracket_width/3 - center_adjust/2]) 
                    rotate([0, 90, 0]) 
                        cylinder(h=2*bracket_thickness, d=screw_diameter, center=true, $fn=256);
            }
        }
    // add posts for holding the washers as weights - up to 5 washers per post
    *translate([-(outer_diameter+washer_post_length-bracket_thickness)/2, 0, (bracket_width+center_adjust)/2])
        rotate([30, 0, 0])
            rotate([0, 90, 0])
                cylinder(h=washer_post_length, d=washer_opening, center=true, $fn=6);
    translate([-washer_post_angled_x1, -washer_post_angled_y1, (bracket_width+center_adjust)/2])
        rotate([30, 0, 0.5*washer_separation_angle])
            rotate([0, 90, 0])
                difference() {
                    cylinder(h=washer_post_length, d=washer_opening, center=true, $fn=6);
                    translate([0, 0, -washer_post_length/4])
                        cylinder(h=washer_post_length, d=screw_diameter, center=true, $fn=256);
                }
    translate([-washer_post_angled_x1, washer_post_angled_y1, (bracket_width+center_adjust)/2])
        rotate([30, 0, -0.5*washer_separation_angle])
            rotate([0, 90, 0])
                difference() {
                    cylinder(h=washer_post_length, d=washer_opening, center=true, $fn=6);
                    translate([0, 0, -washer_post_length/4])
                        cylinder(h=washer_post_length, d=screw_diameter, center=true, $fn=256);
                }
    translate([-washer_post_angled_x2, -washer_post_angled_y2, (bracket_width+center_adjust)/2])
        rotate([30, 0, 1.5*washer_separation_angle])
            rotate([0, 90, 0])
                difference() {
                    cylinder(h=washer_post_length, d=washer_opening, center=true, $fn=6);
                    translate([0, 0, -washer_post_length/4])
                        cylinder(h=washer_post_length, d=screw_diameter, center=true, $fn=256);
                }
    translate([-washer_post_angled_x2, washer_post_angled_y2, (bracket_width+center_adjust)/2])
        rotate([30, 0, -1.5*washer_separation_angle])
            rotate([0, 90, 0])
                difference() {
                    cylinder(h=washer_post_length, d=washer_opening, center=true, $fn=6);
                    translate([0, 0, -washer_post_length/4])
                        cylinder(h=washer_post_length, d=screw_diameter, center=true, $fn=256);
                }
}