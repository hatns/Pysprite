import pygame
class EventHandler():
    def __init__(self):
        self.event_mapper: dict[pygame.event.Event.type: function] = {}
    def add(self, event: pygame.event.Event.type, trigger_function, *function_args):
        if event in self.event_mapper:
            self.event_mapper[event] += ([trigger_function, function_args])
            return
        self.event_mapper[event] = ([trigger_function, function_args])
    def update(self):
        for event in pygame.event.get():
            if event.type in self.event_mapper:
                for i in range(0, len(self.event_mapper[event.type]), 2):
                    self.event_mapper[event.type][i](*self.event_mapper[event.type][i+1])

class GameHandler:
    def __init__(self, functions_to_call, eventhandler, screen, updates_per_second):
        self.funcs = functions_to_call
        self.screen = screen
        self.eventhandler = eventhandler
        self.clock = pygame.time.Clock()
        self.ups = updates_per_second
    
    def update(self):
        for func in self.funcs:
            func()
        pygame.display.update()
        self.clock.tick(self.ups)
        self.eventhandler.update()