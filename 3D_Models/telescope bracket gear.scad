// Lay out the gears that I am going to use for the telescope mount

// the gear library I'm using
use <parametric_involute_gear_v5.0.scad>;

// matching hole for the telescope bracket
bracket_width = 30;

// using a six-sided circle as a hexagon means the hexagon will be slightly smaller than the circle
// circle diameter * cos(30) = hexagon width, flat side to flat side
knob_diameter = bracket_width / cos(30);

// my explicit gear parameters
number_of_teeth = 100;
pitch_diameter = 150;
pressure_angle = 30;
border_width = 10;
gear_thickness = 8;
border_thickness = gear_thickness;
hub_thickness = 13;
circles = 7;

// my derived gear parameters
diametral_pitch = number_of_teeth / pitch_diameter;
echo(str("Diametral Pitch = ", diametral_pitch));
rim_thickness = border_thickness;
rim_width = 0;
hub_diameter = bracket_width + border_width;

// gear parameters I'm not using
clearance = 0;
bore_diameter = 0;
backlash = 0;

// assemble the big gear - remember that its diametral pitch must match the mating gear
difference() {
    // lay out the basic gear
    gear(
        number_of_teeth=number_of_teeth,
        diametral_pitch=diametral_pitch,
        pressure_angle=pressure_angle,
        clearance=clearance,
        gear_thickness=gear_thickness,
        rim_thickness=rim_thickness,
        rim_width=rim_width,
        hub_thickness=hub_thickness,
        hub_diameter=hub_diameter,
        bore_diameter=bore_diameter,
        circles=circles,
        backlash=backlash
    );
    // create the axis type that I expect
    cylinder(h=hub_thickness*2, d=knob_diameter, $fn=6);
}