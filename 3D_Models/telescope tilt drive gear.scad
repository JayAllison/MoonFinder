// Lay out the gears that I am going to use for the telescope mount

// the gear library I'm using
use <parametric_involute_gear_v5.0.scad>;

// my explicit gear parameters
number_of_teeth = 20;
pitch_diameter = 30;
pressure_angle = 30;
border_width = 5;
gear_thickness = 8;
border_thickness = gear_thickness;
hub_thickness = 13;
hub_diameter = 12;
circles = 0;

// my derived gear parameters
diametral_pitch = number_of_teeth / pitch_diameter;
echo(str("Diametral Pitch = ", diametral_pitch));
rim_thickness = border_thickness;
rim_width = border_width;

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
    cube([5, 3, hub_thickness*2], center=true);
}