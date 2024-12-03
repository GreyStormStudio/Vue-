class Vector2 {
    x: number;
    y: number;
    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }

    add(v: Vector2): Vector2 {
        return new Vector2(this.x + v.x, this.y + v.y)
    }

    multiply(s: number): Vector2 {
        return new Vector2(this.x * s, this.y * s)
    }

    dot(v: Vector2): number {
        return this.x * v.x + this.y * v.y
    }

    length(): number {
        return Math.sqrt(this.x * this.x + this.y * this.y)
    }

    normalize(): Vector2 {
        const len = this.length()
        return new Vector2(this.x / len, this.y / len)
    }
}

class RigidBody {
    mass: number;
    airFriction: number;

    position: Vector2;
    velocity: Vector2;
    acceleration: Vector2;

    angle: number;
    angularVelcity: number;
    angularAcceleraion: number;

    forces: Vector2[];
    torque: number;
    constructor(position: Vector2, mass: number, airFriction: number) {
        this.mass = mass;
        this.airFriction = airFriction;
        this.position = position;
        this.velocity = new Vector2(0, 0);
        this.acceleration = new Vector2(0, 0);
        this.angle = 0;
        this.angularVelcity = 0;
        this.angularAcceleraion = 0;
        this.forces = [];
        this.torque = 0;
    }

    applyforce(force: Vector2): void {
        this.forces.push(force)
    }

    applytorque(torque: number): void {
        this.torque += torque
    }

    update(deltaTime: number): void {
        this.acceleration = new Vector2(0, 0)
        const dragForce = this.velocity.normalize().multiply(-this.airFriction * this.velocity.length() * this.velocity.length())
        this.applyforce(dragForce);//应用空气阻力
        for (const force of this.forces) {
            this.acceleration = this.acceleration.add(force.multiply(1 / this.mass))
        }
        this.velocity = this.velocity.add(this.acceleration.multiply(deltaTime));
        this.position = this.position.add(this.velocity.multiply(deltaTime));
        this.forces = [];

        this.angularAcceleraion = this.torque / this.mass;
        this.angularVelcity += this.angularAcceleraion * deltaTime;
        this.angle += this.angularVelcity * deltaTime;
        this.torque = 0;
    }
}

class PhysicsEngine {
    rigidBodies: RigidBody[];
    airFriction: number;
    constructor(airFriction: number) {
        this.rigidBodies = [];
        this.airFriction = airFriction;
    }
    
    addrigidbody(rigidbody: RigidBody) {
        this.rigidBodies.push(rigidbody)
    }

    update(deltaTime: number) {
        for (const body of this.rigidBodies) {
            body.update(deltaTime)
        }
    }
}