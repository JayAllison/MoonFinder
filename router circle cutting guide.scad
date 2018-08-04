// a custom jig for my Rigid router to cut a circle of the specified diameter
// this jig connects into the attachment rod holes that are built into my router's base

// specified parameter - how big of a circle do I want to cut: 8" ~= 203 mm
cut_circle_diameter = 205;

// specified parameter - what size bit am I using: 3/8" ~= 9.5 mm
bit_diameter = 10;

// measurements of my router
rod_depth = 20;
rod_width = 5;
rod_spread = 60;
bit_to_rod_bar_spacing = 65;

// design measurements for the jig
pin_diameter = 4;
disc_height = 18;
shaft_width = 10;
stiffener_height = 3;
stiffener_width = 0.4*3;

// calculated parameters
disc_diameter = pin_diameter*3;
shaft_length = cut_circle_diameter/2 + bit_diameter/2 - bit_to_rod_bar_spacing;
rod_spread_bar_length = rod_spread + rod_width;
shaft_height = shaft_width/2;

// put it all together
union() {
    difference() {
        union() {
            // create the pivot disc
            cylinder(h=disc_height, d=disc_diameter, center=true, $fn=256);
            // attach the extension shaft
            translate([-shaft_length, -shaft_width/2, -disc_height/2])
                cube(size=[shaft_length, shaft_width, shaft_height]);
            // add a stiffening spine to the extension shaft
            translate([-shaft_length, -stiffener_width/2, -disc_height/2+shaft_height])
                cube(size=[shaft_length, stiffener_width, stiffener_height]);
        }
        // punch the pin hole through the pivot disc
        cylinder(h=disc_height*2, d=pin_diameter, center=true, $fn=256);
    }
    // attach the rod spread bar to the shaft
    translate([-shaft_length, -rod_spread_bar_length/2, -disc_height/2]) {
        cube(size=[shaft_width, rod_spread_bar_length, shaft_height]);
    }
    // add a stiffening spine to the rod spread bar
    translate([-shaft_length+shaft_width/2-stiffener_width/2, -rod_spread_bar_length/2, -disc_height/2+shaft_height]) {
        cube(size=[stiffener_width, rod_spread_bar_length, stiffener_height]);
    }
    // attach first rod
    translate([-shaft_length-rod_depth, rod_spread_bar_length/2-rod_width, -disc_height/2])
        cube(size=[rod_depth, rod_width, rod_width]);
    // attach second rod
    translate([-shaft_length-rod_depth, -rod_spread_bar_length/2, -disc_height/2])
        cube(size=[rod_depth, rod_width, rod_width]);
}