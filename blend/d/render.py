#!/usr/bin/env sh
''''exec blender --factory-startup -b "$1" -P "$0" -- "$2" #'''

# $1 .blend
# $2 output dir (contents will be overwritten)

import bpy, os, sys

DIE = bpy.data.objects['Die']
CAMERA_FACE = bpy.data.objects['Camera.Face']
CAMERA_PERSPECTIVE = bpy.data.objects['Camera.Perspective']

OUT_STEM = sys.argv[sys.argv.index('--') + 1]

def render_cam(cam, suffix):
  bpy.context.scene.camera = cam
  bpy.context.scene.render.filepath = os.path.join(OUT_STEM, suffix)
  bpy.ops.render.render(write_still=True)

bpy.context.scene.render.resolution_x = 2048
bpy.context.scene.render.resolution_y = 2048
bpy.context.scene.render.alpha_mode = 'TRANSPARENT'

(start, end) = DIE.animation_data.action.frame_range

bpy.context.scene.frame_set(start)
render_cam(CAMERA_PERSPECTIVE, '0')

for frame in range(int(start), int(end + 1)):
  bpy.context.scene.frame_set(frame)
  render_cam(CAMERA_FACE, str(frame))