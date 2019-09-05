command = ''
started = False
stopped = False
while True:
  command = input(' > ').lower()
  if command == 'start':
    if started:
      print('Car is already started...')
    else:
      started = True
      stopped = False
      print('Car Started...')
  elif command == 'stop':
    if stopped:
      print('Car is already stopped...')
    else:
      stopped = True
      started = False
      print('Car Stopped...')
  elif command == 'help':
    print('''
    start - to start car
    stop - to stop car
    quit - to end program
    ''')
  elif command == 'quit':
    break
  else:
    print('Command not found. Type HELP for support')
