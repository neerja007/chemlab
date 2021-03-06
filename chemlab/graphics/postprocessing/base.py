class AbstractEffect(object):
    '''Interface for a generic post processing effect.
    
    A subclass of AbstractEffect can be used by a
    :class:`~chemlab.graphics.QChemlabWidget` to provide
    post-processing effects such as outlines, gamma correction,
    approximate anti-aliasing, or screen space ambient occlusion.

    '''
    def __init__(self, *args, **kwargs):
        pass
    

    def render(self, fb, textures):
        '''Subclasses should override this method to draw the
        post-processing effect by using the framebuffer *fb*
        (represented as an integer generated by glGenFramebuffers).
        
        The textures corresponding to the model rendering and the
        previous post-processing effects are passed through the
        dictionary *textures*. 
        
        The textures passed by default are "color", "depth" and
        "normal" and are instances of
        :class:`chemlab.graphics.Texture`.

        '''
        raise NotImplementedError()

    def on_resize(self, w, h):
        '''Optionally, subclasses can override on_resize. This method
        is useful if the post-processing effect requires additional
        creation of textures that need to hold multiple passes.

        '''
        pass