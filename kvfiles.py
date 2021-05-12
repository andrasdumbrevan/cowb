### game KV ###
kv = '''
FloatLayout:
    angle: 0
    Image:
        source: "ship3.png"
        
        size_hint_y: 0.7
        size_hint_x: 0.9
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x': .5, 'center_y': .5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: root.angle
                origin: self.center
        canvas.after:
            PopMatrix
'''