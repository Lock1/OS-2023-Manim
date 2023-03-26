void main_interrupt_handler(struct CPURegister cpu, ...) {
    switch (int_number) {
        case PIC1 + IRQ_KEYBOARD:
            keyboard_isr();
            break;
    }
}