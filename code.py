import math

# Function to calculate the radius of SWCNT
def calculate_radius(n, m):
    a = 0.246  # Lattice constant of graphene in nanometers
    radius = (a / (2 * math.pi)) * math.sqrt(n**2 + n*m + m**2)
    return radius

# Function to calculate the chiral angle
def calculate_chiral_angle(n, m):
    if n == 0:
        return 0
    chiral_angle = math.degrees(math.atan((math.sqrt(3) * m) / (2 * n + m)))
    return chiral_angle

# Function to determine chirality
def determine_chirality(n, m):
    if n == m:
        return "Armchair"
    elif n == 0 or m == 0:
        return "Zigzag"
    else:
        return "Chiral"

# Function to calculate the translational repeat unit T
def calculate_translational_unit(n, m, a):
    gcd_val = math.gcd(2*n + m, n + 2*m)
    T = (math.sqrt(3) * a * math.sqrt(n**2 + m**2 + n*m)) / gcd_val
    return T

# Function to calculate high-symmetry points
def calculate_high_symmetry_points(T):
    k_z = math.pi / T
    gamma_point = (0, 0, 0)
    z_point = (0, 0, k_z)
    return gamma_point, z_point

# Main function
def main():
    try:
        n = int(input("Enter the value of n: "))
        m = int(input("Enter the value of m: "))
        a_input = input("Enter the lattice constant (default is 0.246 nm): ")
        a = float(a_input) if a_input else 0.246  # Default lattice constant of graphene in nanometers
        
        radius = calculate_radius(n, m)
        chiral_angle = calculate_chiral_angle(n, m)
        chirality = determine_chirality(n, m)
        T = calculate_translational_unit(n, m, a)
        gamma_point, z_point = calculate_high_symmetry_points(T)
        
        print(f"Radius of the SWCNT: {radius:.3f} nm")
        print(f"Chiral angle: {chiral_angle:.3f} degrees")
        print(f"Chirality: {chirality}")
        print(f"Translational repeat unit T: {T:.3f} nm")
        print(f"Gamma point: {gamma_point}")
        print(f"Z point: {z_point}")
    
    except ValueError:
        print("Please enter valid numeric values for n, m, and the lattice constant.")

if __name__ == "__main__":
    main()
