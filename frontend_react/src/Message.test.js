import React from 'react';
import { render, screen } from '@testing-library/react';
import Message from './Message';

test('renders Hello, World! message', () => {
    render(<Message />);
    const messageElement = screen.getByText(/Hello, World!/i);
    expect(messageElement).toBeInTheDocument();
});
