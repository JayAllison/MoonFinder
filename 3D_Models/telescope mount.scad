// edit these values to configure the mount
mount_thickness = 8;
mount_top_width = 24;
mount_bottom_width = 88;
mount_bottom_side_height = 32;
mount_height = 160;

motor_diameter = 28;
motor_offset_from_axle = 50;

axle_diameter = 6;

screw_diameter = 3.5;

// these values are calculated - do not edit

// from the documentation - how to make a triangular solid
module prism(l, w, h){
   polyhedron(
       points=[[0,0,0], [l,0,0], [l,w,0], [0,w,0], [0,w,h], [l,w,h]],
       faces=[[0,1,2,3], [5,4,3,2], [0,4,5,1], [0,3,4], [5,2,1]]
   );
}

difference() {
    // start with a big cube to subtract from
    cube(size=[mount_thickness, mount_bottom_width, mount_height], center=false);
    // lop off the top-left corner
    translate([-mount_thickness/2,(mount_bottom_width-mount_top_width)/2,mount_height])
        rotate([180,0,0])
            prism(mount_thickness*2, (mount_bottom_width-mount_top_width)/2, mount_height-mount_bottom_side_height);
    // lop off the top-right corner
    translate([mount_thickness,mount_top_width+(mount_bottom_width-mount_top_width)/2,mount_height])
        rotate([0,180,0])
            prism(mount_thickness*2, (mount_bottom_width-mount_top_width)/2, mount_height-mount_bottom_side_height);
    // punch the axle hole through
    translate([mount_thickness/2,mount_bottom_width/2,mount_height-mount_top_width/2])
        rotate([0,90,0])
            cylinder(h=mount_thickness*2, d=axle_diameter, center=true, $fn=256);
    // create space for the motor to be mounted
    translate([mount_thickness/2,mount_bottom_width/2,mount_height-motor_offset_from_axle])
        rotate([0,90,0])
            cylinder(h=mount_thickness*2, d=motor_diameter, center=true, $fn=256);
    // create space for the motor to be mounted (and to save print time)
    translate([mount_thickness/2,mount_bottom_width/2,mount_bottom_side_height+motor_diameter/2])
        rotate([0,90,0])
            cylinder(h=mount_thickness*2, d=motor_diameter, center=true, $fn=256);
    translate([-mount_thickness/2,mount_bottom_width/2-motor_diameter/2,mount_bottom_side_height+motor_diameter/2])
        cube([mount_thickness*2, motor_diameter, mount_height-motor_offset_from_axle-mount_bottom_side_height-motor_diameter/2], center=false);
}