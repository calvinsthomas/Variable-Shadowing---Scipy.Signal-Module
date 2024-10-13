"""# Alpha renaming scipy.signal - Toy Ex.
# Boolean flag to control variable shadowing strategy"""
rename_import = True  # Set as False chooses Option 2

# Conditional import and variable naming using alpha renaming
if rename_import:
    # Option 1: Rename imported scipy.signal module as signal_ind and use 'signal_main' as variable
    from scipy import signal as signal_ind

    # Main Reusable Var. Name: 'signal_main'. NOTE: LOW HANGING FRUIT APPLIED TO OUR VARIABLE NAMING DATA AND RENAMING FOR EACH EX. FILTERED PROCESS.
    signal_main = compute_signal(data)

    # Use 'signal_ind' for scipy.signal module funcs.
    b, a = signal_ind.butter(3, 0.05)
    filtered_data = signal_ind.filtfilt(b, a, signal_main)
else:
    # Option 2: Keep imported module name as 'signal' and rename variable to 'signal_f'
    from scipy import signal

    # Main reused var., name: 'signal_f'
    signal_f = compute_signal(data)

    # Use 'signal' for scipy.signal module functions, and 'signal_f' for our reusable var. named signal!
    b, a = signal.butter(3, 0.05)
    filtered_data = signal.filtfilt(b, a, signal_f)
